import itertools as it
import numpy as np

WORD_LIST = []
with open('data/possible_words.txt') as f:
    for word in f.readlines():
        WORD_LIST += [word.strip()]

WORD_FREQ = dict()
with open("data/short_freqs.txt") as fp:
    for line in fp.readlines():
        pieces = line.split(' ')
        word = pieces[0]
        freqs = [
            float(piece.strip())
            for piece in pieces[1:]
        ]
        WORD_FREQ[word] = np.mean(freqs[-5:])

PATTERN_COMBINATIONS = np.array(list(it.product([0, 1, 2], repeat=5)))