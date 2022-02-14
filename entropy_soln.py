import os
import numpy as np
import itertools as it
from scipy import stats
import json

#WORD_LIST = os.path.join(DATA_DIR, "possible_words.txt")
#WORD_FREQ_FILE = os.path.join(DATA_DIR, "short_freqs.txt")

d = {0: "NO", 1: "IN-WORD", 2: "EXACT"}

WORD_LIST = []

with open('possible_words.txt') as f:
    for word in f.readlines():
        WORD_LIST += [word.strip()]

WORD_FREQ = dict()
with open("short_freqs.txt") as fp:
    for line in fp.readlines():
        pieces = line.split(' ')
        word = pieces[0]
        freqs = [
            float(piece.strip())
            for piece in pieces[1:]
        ]
        WORD_FREQ[word] = np.mean(freqs[-5:])


arr = [0, 1, 2]
pattern_combinations = np.array(list(it.product(arr, repeat=5)))

test_word_list = ["slear", "nrash", "realt", "crane"]
test_comb = np.array([0,1,2,0,1])
test_comb_d = [d[pattern] for pattern in test_comb]

def wordchecker(wordlist, test_word, pattern):
    # n.b. for loops won't run if number n (where pattern == n) isn't found
    output_d = {}
    for i in range(0,len(wordlist)):
        wordcheck = wordlist[i]
        equalmat = np.zeros(5)

        # check 2s (you guess the exact word)
        for item in np.where(pattern == 2)[0]:
            if test_word[item] == wordcheck[item]:
                equalmat[item] = 1
            else:
                equalmat[item] = 0

        # check for 1s
        for item in np.where(pattern == 1)[0]:
            if test_word[item] in wordcheck:
                equalmat[item] = 1
            else:
                equalmat[item] = 0

        # check for 0s
        for item in np.where(pattern == 0)[0]:
            if test_word[item] not in wordcheck:
                equalmat[item] = 1
            else:
                equalmat[item] = 0
        if np.sum(equalmat) == 5:
            output_d[wordcheck] = True
        else:
            output_d[wordcheck] = False
    return output_d

#print(wordchecker(test_word_list, "crane", np.array([2,2,2,1,1])))

def find_prob_distribution(wordlist, word):
    px = []
    tot = float(len(wordlist))
    for pattern in pattern_combinations:
        wordcheck_d = wordchecker(wordlist, word, pattern)
        num_true = sum(wordcheck_d.values())
        px += [num_true/tot]
        #print(tot)
    return np.array(px)
#prob_dist = find_prob_distribution(test_word_list, "crane")
#print(prob_dist)

def create_entropy_data(possible_words):
    ent = {}
    for word in possible_words:
        prob_dist = find_prob_distribution(WORD_LIST, word)
        ent[word] = stats.entropy(prob_dist)
    with open('word_entropy_initial.json', 'w+') as f:
        # this would place the entire output on one line
        # use json.dump(ent, f, indent=4) to "pretty-print" with four spaces per indent
        json.dump(ent, f, indent=4)
    return ent

ent_1 = create_entropy_data(WORD_LIST)
