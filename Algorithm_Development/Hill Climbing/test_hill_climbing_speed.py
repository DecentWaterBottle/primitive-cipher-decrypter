import re, sys, os
from hill_climbing import hill_climbing
import numpy as np
from matplotlib import pyplot as plt
from timeit import default_timer as timer

current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
sys.path.append(parent_directory)

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

average_time_scores = {20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0, 2000: 0, 5000: 0}

for key, value in test_files.items():
    inner_averages = []

    # Text 1
    f = open(value + "/text_1.txt", "r", encoding="utf-8")
    words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()
    start = timer()
    hill_climbing(words)
    end = timer()
    inner_averages.append(end - start)

    # Text 2
    f = open(value + "/text_2.txt", "r", encoding="utf-8")
    words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()
    start = timer()
    hill_climbing(words)
    end = timer()
    inner_averages.append(end - start)

    # Text 3
    f = open(value + "/text_3.txt", "r", encoding="utf-8")
    words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()
    start = timer()
    hill_climbing(words)
    end = timer()
    inner_averages.append(end - start)

    # Text 4
    f = open(value + "/text_4.txt", "r", encoding="utf-8")
    words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()
    start = timer()
    hill_climbing(words)
    end = timer()
    inner_averages.append(end - start)

    # Text 5
    f = open(value + "/text_5.txt", "r", encoding="utf-8")
    words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()
    start = timer()
    hill_climbing(words)
    end = timer()
    inner_averages.append(end - start)


    average = sum(inner_averages) / 2
    print(average)
    averages.append(average)


print(averages)
plt.title("Hill-Climbing Time Taken (Quadgrams)")
plt.xlabel("Character Count")
plt.ylabel("Speed (seconds)")
plt.plot(np.array([20, 50, 100, 200, 500, 1000, 2000, 5000]).astype("str"), averages)
plt.show()




