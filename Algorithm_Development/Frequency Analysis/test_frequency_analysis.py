import re, sys, os
from main import perform_frequency_analysis
import numpy as np
from matplotlib import pyplot as plt

current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
sys.path.append(parent_directory)
from Algorithm_Development.accuracy_test import test_accuracy
import matplotlib as mpl
mpl.use('TkAgg')


alphabet = "abcdefghijklmnopqrstuvwxyz"
word_count = []
accuracy_list = []

# Get encrypted test files
test_files = []
for root, dirs, files in os.walk("../Test_Texts/Encrypted"):
    print(f"Root: {root}, Dirs: {dirs}, Files: {files}")
    for file in files:
        test_files.append(root + "/" + file)

# Perform frequency analysis
for file in test_files:
    key_string = ""
    f = open(file, "r", encoding="utf-8")
    words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()
    word_count.append(len(words.split(" ")))
    letter_frequency_mapping = perform_frequency_analysis(words)
    accuracy_list.append(test_accuracy(letter_frequency_mapping))

    for key, value in letter_frequency_mapping.items():
        key_string += value
    mapping = str.maketrans(alphabet, key_string)
    words = words.translate(mapping)
    print(words)


# Sort the word counts and accuracies relative to each other using word count
sort = np.argsort(np.array(word_count))
word_count = np.array(word_count)[sort]
accuracy_list = np.array(accuracy_list)[sort]

for i in range(len(accuracy_list)):
    print(f"Accuracy for word count {word_count[i]} is {accuracy_list[i]}/26")

plt.title("Frequency Analysis")
plt.xlabel("Word Count")
plt.ylabel("Accuracy")
plt.ylim(0, 26)
plt.plot(word_count, accuracy_list)
plt.show()
