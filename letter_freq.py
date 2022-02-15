import numpy as np

WORD_LIST = []

with open('possible_words.txt') as f:
    for word in f.readlines():
        WORD_LIST += [word.strip()]

freq = {}
for i in range(0, 26):
    freq[chr(ord('`')+i+1)] = np.zeros(5)

for word in WORD_LIST:
    for i in range(0,len(word)):
        freq[word[i]][i] = freq[word[i]][i] + 1

print(freq['a'])
