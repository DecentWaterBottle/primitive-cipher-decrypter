import random
import math



# Get quadgrams from english_quadgrams.txt and convert into dictionary
# Key: Quadgram    --     Value: frequency
def get_quadgrams():
    quadgrams = {}
    with open("english_quadgrams.txt") as file:
        for line in file:
            line = line.split()
            quadgram = line[0]
            frequency = line[1]
            quadgrams[quadgram.lower()] = int(frequency)
    return quadgrams


def find_score(text, quadgrams):
    score = 0
    # -3 to avoid getting an out-of-bounds exception when attempting to read +4 chars ahead of i
    for i in range(len(text)-3):
        # Get the quadgram
        cur_quadgram = text[i:i+4]
        # Check if the quadgram is in the list of quadgrams
        if cur_quadgram in quadgrams:
            # If so, use log10 for numerical stability and to compress the quadgram frequencies
            # to a smaller scale. Thus quadgrams with a low frequency will not become dwarfed by those
            # with a far significantly higher frequency.
            score += math.log10(quadgrams[cur_quadgram])
        # else:
        #     score -= 15
    return score


def decrypt_text(text, key):
    mapping = str.maketrans("".join(key.keys()), "".join(key.values()))
    text = text.lower()
    decrypted_text = text.translate(mapping)
    return decrypted_text


# Shuffle the alphabet to get a random starting key
def shuffle_alphabet():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(alphabet)
    shuffled_alphabet = "".join(alphabet)
    return dict(zip(alphabet, shuffled_alphabet))


def main():
    quadgrams = get_quadgrams()
    ciphertext = 'dj dk c qlxdwi wf sdgdu pcx. xlrlu kqcslkbdqk, kjxdhdet fxwz c bdiile rckl, bcgl pwe jbldx fdxkj ' \
                 'gdsjwxo ctcdekj jbl lgdu tcucsjds lzqdxl. iyxdet jbl rcjjul, xlrlu kqdlk zcectli jw kjlcu klsxlj ' \
                 'qucek jw jbl lzqdxl’k yujdzcjl plcqwe, jbl ilcjb kjcx, ce cxzwxli kqcsl kjcjdwe pdjb lewytb qwplx ' \
                 'jw ilkjxwo ce lejdxl qucelj. qyxkyli ro jbl lzqdxl’k kdedkjlx ctlejk, qxdeslkk uldc xcslk bwzl ' \
                 'crwcxi blx kjcxkbdq, sykjwidce wf jbl kjwule qucek jbcj sce kcgl blx qlwqul cei xlkjwxl fxlliwz jw ' \
                 'jbl tcucvo… '


    counter = 0
    overall_best_score = 0
    overall_best_key = ""
    for i in range(20):
        best_key = shuffle_alphabet()
        decrypted_text = decrypt_text(ciphertext, best_key)
        best_score = find_score(decrypted_text, quadgrams)
        for i in range(2000):
            new_key = best_key.copy()
            a, b = random.sample("abcdefghijklmnopqrstuvwxyz", 2)
            new_key[a], new_key[b] = new_key[b], new_key[a]

            text_decrypted_with_new_key = decrypt_text(ciphertext, new_key)
            new_score = find_score(text_decrypted_with_new_key, quadgrams)
            # print(f"New Score {new_score}, best score: {best_score}")
            if new_score > best_score:
                # print("Score is better")
                counter += 1
                best_key = new_key
                best_score = new_score

        if best_score > overall_best_score:
            overall_best_score = best_score
            overall_best_key = best_key

    print(overall_best_key)
    print(overall_best_score)
    print(decrypt_text(ciphertext, overall_best_key))



# Star wars mapping: {'a': 'z', 'h': 'k', 't': 'g', 'f': 'f', 'e': 'n', 'n': 'j', 'g': 'v', 'v': 'x', 'y': 'u', 'c': 'a', 'r': 'b', 'i': 'd', 'u': 'l', 'd': 'i', 'q': 'p', 'o': 'y', 'p': 'w', 'x': 'r', 's': 'c', 'j': 't', 'z': 'm', 'k': 's', 'w': 'o', 'm': 'q', 'b': 'h', 'l': 'e'}

main()

