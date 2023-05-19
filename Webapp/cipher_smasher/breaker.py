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


def hill_climbing(ciphertext):
    quadgrams = get_quadgrams()
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
            if new_score > best_score:
                counter += 1
                best_key = new_key
                best_score = new_score

        if best_score > overall_best_score:
            overall_best_score = best_score
            overall_best_key = best_key

    plain_text = decrypt_text(ciphertext, overall_best_key)
    return plain_text, overall_best_key, overall_best_score
