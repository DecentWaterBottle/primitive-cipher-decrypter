import re, sys, os

current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
sys.path.append(parent_directory)

from Algorithm_Development.accuracy_test import test_accuracy
letter_frequency_in_text = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0,
                            "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0,
                            "w": 0, "x": 0, "y": 0, "z": 0}

letter_frequency_mapping = {"a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": "", "h": "", "i": "", "j": "",
                            "k": "", "l": "", "m": "", "n": "", "o": "", "p": "", "q": "", "r": "", "s": "", "t": "",
                            "u": "", "v": "", "w": "", "x": "", "y": "", "z": ""}

actual_mapping = {"a": "k", "b": "x", "c": "v", "d": "m", "e": "c", "f": "y", "g": "o", "h": "p", "i": "h", "j": "q",
                            "k": "r", "l": "s", "m": "z", "n": "f", "o": "i", "p": "j", "q": "a", "r": "d", "s": "l", "t": "e",
                            "u": "g", "v": "w", "w": "b", "x": "u", "y": "n", "z": "t"}

english_letter_frequencies = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "d", "l",  "u", "c", "m", "f",
                              "y", "w",  "g", "p", "b", "v", "k", "x", "q", "j", "z"]

alphabet = "abcdefghijklmnopqrstuvwxyz"

key_string = ""

# Extract words
f = open("../Test_Texts/Encrypted/encrypted_long_story.txt", "r", encoding="utf-8")
words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()


# Find frequency of letters
for key, value in letter_frequency_in_text.items():
    for letter in words:
        if letter == key:
            letter_frequency_in_text[key] += 1

letter_frequency_in_text = sorted(letter_frequency_in_text.items(), key=lambda x: x[1], reverse=True)
print("Letter Frequency: ", letter_frequency_in_text)


# Map English letter frequencies to input letter frequencies
for i in range(len(letter_frequency_in_text)):
    print(
        f"Letter: {letter_frequency_in_text[i]} being set to: {english_letter_frequencies[i]}")
    letter_frequency_mapping[(letter_frequency_in_text[i][0])] = english_letter_frequencies[i]

print(f"Complete Mapping: {letter_frequency_mapping}")


for key, value in letter_frequency_mapping.items():
    key_string += value

print(key_string)
print(alphabet)
mapping = str.maketrans(alphabet, key_string)
words = words.translate(mapping)

print(words)
print(f"Accuracy: {test_accuracy(letter_frequency_mapping)}")
print(actual_mapping)
print(letter_frequency_mapping)

