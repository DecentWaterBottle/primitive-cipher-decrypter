import random
import math
import sys
from timeit import default_timer as timer

import numpy as np


# Get quadgrams from english_quadgrams.txt and convert into dictionary
# Key: Quadgram    --     Value: frequency

translate_times = []
find_score_times = []


def get_quadgrams():
    quadgrams = {}
    with open("english_quadgrams.txt") as file:
        for line in file:
            line = line.split()
            quadgram = line[0]
            frequency = line[1]
            quadgrams[quadgram.lower()] = int(frequency)
    return quadgrams


def get_bigrams():
    bigrams = {}
    with open("english_bigrams.txt") as file:
        for line in file:
            line = line.split()
            bigram = line[0]
            frequency = line[1]
            bigrams[bigram.lower()] = int(frequency)
    return bigrams


def process_quadgrams(quadgrams):
    integer_quadgrams = {}
    for quadgram, frequency in quadgrams.items():
        new_quadgram = (ord(quadgram[0]) << 24) + (ord(quadgram[1]) << 16) + (ord(quadgram[2]) << 8) + (ord(quadgram[3]))
        integer_quadgrams[new_quadgram] = math.log10(frequency)

    return integer_quadgrams


def find_score(text, quadgrams, biOrQuad="bi"):
    start = timer()
    if biOrQuad == "bi":
        score = 0
        # -3 to avoid getting an out-of-bounds exception when attempting to read +4 chars ahead of i
        for i in range(len(text) - 1):
            # Get the quadgram
            cur_quadgram = text[i:i + 2]
            # cur_quadgram = ''.join(text[i:i + 4])
            # Check if the quadgram is in the list of quadgrams
            if cur_quadgram in quadgrams:
                # If so, use log10 for numerical stability and to compress the quadgram frequencies
                # to a smaller scale. Thus quadgrams with a low frequency will not become dwarfed by those
                # with a far significantly higher frequency.
                score += math.log10(quadgrams[cur_quadgram])

    else:
        score = 0
        # -3 to avoid getting an out-of-bounds exception when attempting to read +4 chars ahead of i
        for i in range(len(text)-3):
            # Get the quadgram
            cur_quadgram = text[i:i+4]
            # cur_quadgram = ''.join(text[i:i + 4])
            # Check if the quadgram is in the list of quadgrams
            if cur_quadgram in quadgrams:
                # If so, use log10 for numerical stability and to compress the quadgram frequencies
                # to a smaller scale. Thus quadgrams with a low frequency will not become dwarfed by those
                # with a far significantly higher frequency.
                score += math.log10(quadgrams[cur_quadgram])
            # else:
            #     score -= 15
    end = timer()
    find_score_times.append(end-start)
    return score




def find_score_integer_arithmetic(text, quadgrams):
    score = 0
    for i in range(len(text) - 3):
        quadgram = (ord(text[i]) << 24) + (ord(text[i+1]) << 16) + (ord(text[i+2]) << 8) + (ord(text[i+3]))
        if quadgram in quadgrams:
            score += quadgrams[quadgram]

    return score


def decrypt_text(text, key):
    start = timer()
    mapping = str.maketrans("".join(key.keys()), "".join(key.values()))
    text = text.lower()
    decrypted_text = text.translate(mapping)
    end = timer()
    translate_times.append(end-start)
    return decrypted_text


# Shuffle the alphabet to get a random starting key
def shuffle_alphabet():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(alphabet)
    shuffled_alphabet = "".join(alphabet)
    return dict(zip(alphabet, shuffled_alphabet))


def find_maximum(current_key, cipher_text, max_fitness, quadgrams):
    better_key_found = False
    for i, (ch1, pos1) in enumerate(current_key.items()):
        for ch2, pos2 in list(current_key.items())[i+1:]:
            # Swap i-th and j-th characters of the alphabet
            new_key = current_key.copy()
            new_key[ch1] = pos2
            new_key[ch2] = pos1
            new_fitness = find_score(decrypt_text(cipher_text, new_key), quadgrams, biOrQuad="quad")
            if new_fitness > max_fitness:
                max_fitness = new_fitness
                current_key = new_key
                better_key_found = True

    # print(f"{better_key_found}, {current_key}, {max_fitness}, {new_fitness}")
    # print(f"Better key found? {better_key_found}. {new_fitness} is not better than {max_fitness}")
    return better_key_found, current_key, max_fitness


def simulated_annealing():
    T = 1.0
    cooling_rate = 0.01
    current_key = shuffle_alphabet()
    current_score = find_score(decrypt_text(ciphertext, current_key), quadgrams)
    while T > 0.0000001:
        new_key = current_key.copy()
        a, b = random.sample("abcdefghijklmnopqrstuvwxyz", 2)
        new_key[a], new_key[b] = new_key[b], new_key[a]

        new_score = find_score(decrypt_text(ciphertext, new_key), quadgrams)
        delta = new_score - current_score
        delta_threshold = 100
        if delta > delta_threshold:
            p = 1e-100
        else:
            # p = math.exp(delta / T)
            p = np.exp(delta / T)

        if random.random() < p:
            current_key = new_key
            current_score = new_score
        T *= 1 - cooling_rate

def hill_climbing_all_key_swap(quadgrams):
    maximum_hit = 0
    best_key = shuffle_alphabet()
    best_score = 0
    inner_best_key = 0
    for i in range(30):
        print(i)
        current_key = shuffle_alphabet()
        inner_best_score = 0

        while True:
            better_key_found, new_key, new_score = find_maximum(current_key, ciphertext, inner_best_score, quadgrams)
            if not better_key_found:
                break
            else:
                if new_score > inner_best_score:
                    inner_best_score = new_score
                    inner_best_key = new_key
                current_key = new_key

        if new_score > best_score:
            best_score = new_score
            maximum_hit = 1
            best_key = inner_best_key
        elif new_score == best_score:
            # print(f"New Score {new_score} == best score {best_score}")
            maximum_hit += 1
            if maximum_hit > 5:
                print("Local Maximum Hit")
                break

    print(f"Best Score: {best_score}")
    print(f"{decrypt_text(ciphertext, best_key)}")


def hill_climbing(ciphertext=""):
    start = timer()
    quadgrams = get_quadgrams()
    bigrams = get_bigrams()
    # quadgrams = process_quadgrams(text_quadgrams)

    print(ciphertext)
    print(f"New Size: {sys.getsizeof(quadgrams)}")
    print(f"New Size: {sys.getsizeof(bigrams)}")

    counter = 0
    overall_best_score = 0
    overall_best_key = ""
    local_maximum = 0
    for i in range(20):
        print(i)
        best_key = shuffle_alphabet()
        decrypted_text = decrypt_text(ciphertext, best_key)
        best_score = find_score(decrypted_text, quadgrams, biOrQuad="quad")
        for i in range(2000):
            new_key = best_key.copy()
            a, b = random.sample("abcdefghijklmnopqrstuvwxyz", 2)
            new_key[a], new_key[b] = new_key[b], new_key[a]

            text_decrypted_with_new_key = decrypt_text(ciphertext, new_key)
            new_score = find_score(text_decrypted_with_new_key, quadgrams, biOrQuad="quad")
            if new_score > best_score:
                counter += 1
                best_key = new_key
                best_score = new_score

        if best_score > overall_best_score:
            overall_best_score = best_score
            overall_best_key = best_key
            local_maximum = 1
        elif best_score == overall_best_score:
            print("Local maximum hit once")
            local_maximum += 1
            if local_maximum == 3:
                print("Local Maximum Reached")
                break

    print(f"Decrypted Text: {decrypt_text(ciphertext, overall_best_key)}")

    end = timer()
    print(f"Time taken: {end - start} seconds")
    return overall_best_key


ciphertext = 'dj dk c qlxdwi wf sdgdu pcx. xlrlu kqcslkbdqk, kjxdhdet fxwz c bdiile rckl, bcgl pwe jbldx fdxkj ' \
             'gdsjwxo ctcdekj jbl lgdu tcucsjds lzqdxl. iyxdet jbl rcjjul, xlrlu kqdlk zcectli jw kjlcu klsxlj ' \
             'qucek jw jbl lzqdxl’k yujdzcjl plcqwe, jbl ilcjb kjcx, ce cxzwxli kqcsl kjcjdwe pdjb lewytb qwplx ' \
             'jw ilkjxwo ce lejdxl qucelj. qyxkyli ro jbl lzqdxl’k kdedkjlx ctlejk, qxdeslkk uldc xcslk bwzl ' \
             'crwcxi blx kjcxkbdq, sykjwidce wf jbl kjwule qucek jbcj sce kcgl blx qlwqul cei xlkjwxl fxlliwz jw ' \
             'jbl tcucvo… '

best_key = hill_climbing(ciphertext=ciphertext)

# quadgram times:
#   Translate: 0.00003789278499268631.
#   Score:     0.00020478140310830446

# bigram times
#   Translate: 0.00003779942819277949
#   Score:     0.00021408081638866848

# John gazed into the shimmering pool before him. The reflections of those around him glimmered in the bright water, illuminated by the lantern one of his companions carried. It had been a long journey to reach this point but they had finally arrived. Despite all the odds and the countless others who had attempted this journey and failed, they had finally achieved what nobody before them could. John contained him emotions and remained focused on the task at hand. However, in reality he was tired, hungry and badly in need of rest. He could see his own feelings reflected on the faces of those with him.
