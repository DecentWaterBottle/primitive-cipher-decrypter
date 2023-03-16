import re, sys, os
from hill_climbing import hill_climbing
import numpy as np
from matplotlib import pyplot as plt


test_files = []
for root, dirs, files in os.walk("../Test_Texts/character_based/encrypted"):
    print(f"Root: {root}, Dirs: {dirs}, Files: {files}")
    for file in files:
        test_files.append(root + "/" + file)


for file in test_files:
    key_string = ""
    f = open(file, "r", encoding="utf-8")
    words = " ".join(re.findall("[a-zA-Z]+", f.read())).lower()