import random
import math

quadgrams = {}

with open("english_quadgrams.txt") as file:
    for line in file:
        line = line.split()
        quadgram = line[0]
        frequency = line[1]
        quadgrams[quadgram] = frequency
