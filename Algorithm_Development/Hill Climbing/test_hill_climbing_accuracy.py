import re, sys, os
from hill_climbing import hill_climbing
import numpy as np
from matplotlib import pyplot as plt

current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
sys.path.append(parent_directory)
from Algorithm_Development.accuracy_test import test_accuracy_with_custom_mapping


test_files = {}

# Get list of directories containing characters
directories = (os.listdir("../Test_Texts/character_based/Encrypted"))
# Remove the _chars from the end
for i in range(len(directories)):
    directories[i] = int(directories[i].replace("_chars", ""))

# Sort directories in order from the least characters -> most characters
directories.sort()
print(directories)
averages = []

# Add the files found to the dictionary containing file names for each character count
for directory in directories:
    test_files[directory] = "../Test_Texts/character_based/Encrypted/" + str(directory) + "_chars"

average_frequency_scores = {20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0, 2000: 0, 5000: 0}

for key, value in test_files.items():
    averages_list = []

    # Text 1
    f = open(value + "/text_1.txt", "r", encoding="utf-8")
    words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()
    letter_frequency_mapping = hill_climbing(words)
    # qwertyuiopasdfghjklzxcvbnm
    actual_mapping = {"a": "q", "b": "w", "c": "e", "d": "r", "e": "t", "f": "y", "g": "u", "h": "i", "i": "o",
                      "j": "p",
                      "k": "a", "l": "s", "m": "d", "n": "f", "o": "g", "p": "h", "q": "j", "r": "k", "s": "l",
                      "t": "z",
                      "u": "x", "v": "c", "w": "v", "x": "b", "y": "n", "z": "m"}
    actual_mapping = {v: k for k, v in actual_mapping.items()}
    print(f"PREDICTED MAPPING: {letter_frequency_mapping}")
    print(f"ACTUAL MAPPING: {actual_mapping}")
    averages_list.append(test_accuracy_with_custom_mapping(letter_frequency_mapping, actual_mapping, show_output=True))
    print()

    # Text 2
    f = open(value + "/text_2.txt", "r", encoding="utf-8")
    words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()
    letter_frequency_mapping = hill_climbing(words)
    # kxvmcnophqrszyijadlegwbuft
    actual_mapping = {"a": "k", "b": "x", "c": "v", "d": "m", "e": "c", "f": "n", "g": "o", "h": "p", "i": "h",
                      "j": "q",
                      "k": "r", "l": "s", "m": "z", "n": "y", "o": "i", "p": "j", "q": "a", "r": "d", "s": "l",
                      "t": "e",
                      "u": "g", "v": "w", "w": "b", "x": "u", "y": "f", "z": "t"}
    actual_mapping = {v: k for k, v in actual_mapping.items()}
    averages_list.append(test_accuracy_with_custom_mapping(letter_frequency_mapping, actual_mapping))

    # Text 3
    f = open(value + "/text_3.txt", "r", encoding="utf-8")
    words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()
    letter_frequency_mapping = hill_climbing(words)
    # ebfaswlygqtzohdkucprnxivmj
    actual_mapping = {"a": "e", "b": "b", "c": "f", "d": "a", "e": "s", "f": "w", "g": "l", "h": "y", "i": "g",
                      "j": "q",
                      "k": "t", "l": "z", "m": "o", "n": "h", "o": "d", "p": "k", "q": "u", "r": "c", "s": "p",
                      "t": "r",
                      "u": "n", "v": "x", "w": "i", "x": "v", "y": "m", "z": "j"}
    actual_mapping = {v: k for k, v in actual_mapping.items()}
    averages_list.append(test_accuracy_with_custom_mapping(letter_frequency_mapping, actual_mapping))

    # Text 4
    f = open(value + "/text_4.txt", "r", encoding="utf-8")
    words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()
    letter_frequency_mapping = hill_climbing(words)
    # hmftkqderyzjbgpuawosnxicvl
    actual_mapping = {"a": "h", "b": "m", "c": "f", "d": "t", "e": "k", "f": "q", "g": "d", "h": "e", "i": "r",
                      "j": "y",
                      "k": "z", "l": "j", "m": "b", "n": "g", "o": "p", "p": "u", "q": "a", "r": "w", "s": "o",
                      "t": "s",
                      "u": "n", "v": "x", "w": "i", "x": "c", "y": "v", "z": "l"}
    actual_mapping = {v: k for k, v in actual_mapping.items()}
    averages_list.append(test_accuracy_with_custom_mapping(letter_frequency_mapping, actual_mapping))

    # Text 5
    f = open(value + "/text_5.txt", "r", encoding="utf-8")
    words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()
    letter_frequency_mapping = hill_climbing(words)
    # ctlsxahgbpreqjumkowvifdyzn
    actual_mapping = {"a": "c", "b": "t", "c": "l", "d": "s", "e": "x", "f": "a", "g": "h", "h": "g", "i": "b",
                      "j": "p",
                      "k": "r", "l": "e", "m": "q", "n": "j", "o": "u", "p": "m", "q": "k", "r": "o", "s": "w",
                      "t": "v",
                      "u": "i", "v": "f", "w": "d", "x": "y", "y": "z", "z": "n"}
    actual_mapping = {v: k for k, v in actual_mapping.items()}
    averages_list.append(test_accuracy_with_custom_mapping(letter_frequency_mapping, actual_mapping))

    average = sum(averages_list) / 5
    averages.append(average)


print(averages)
plt.title("Hill-Climbing Accuracy (Quadgrams)")
plt.xlabel("Character Count")
plt.ylabel("Accuracy")
plt.ylim(0, 26)
plt.plot(np.array([20, 50, 100, 200, 500, 1000, 2000, 5000]).astype("str"), averages)
plt.show()





