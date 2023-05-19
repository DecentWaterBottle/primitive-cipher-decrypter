import sys, os, re

current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
sys.path.append(parent_directory)

alphabet = "abcdefghijklmnopqrstuvwxyz"


# Extract words
def perform_frequency_analysis(words):
    letter_frequency_in_text = {}
    letter_frequency_mapping = {}

    english_letter_frequencies = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "d", "l", "u", "c", "m", "f",
                                  "y", "w", "g", "p", "b", "v", "k", "x", "q", "j", "z"]

    # Find frequency of letters
    for letter in alphabet:
        frequency = words.count(letter)
        letter_frequency_in_text[letter] = frequency
    # print(words)
    print(letter_frequency_in_text)

    letter_frequency_in_text = sorted(letter_frequency_in_text.items(), key=lambda x: x[1], reverse=True)

    # Map English letter frequencies to input letter frequencies
    for i in range(len(letter_frequency_in_text)):
        letter_frequency_mapping[(letter_frequency_in_text[i][0])] = english_letter_frequencies[i]

    print(letter_frequency_mapping)
    return letter_frequency_mapping


f = open("../Test_Texts/Encrypted/5000_story01_encrypted.txt", "r", encoding="utf-8")
words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()
letter_frequency_mapping = perform_frequency_analysis(words)
key_string = ""

for key, value in letter_frequency_mapping.items():
    key_string += value

f.close()
