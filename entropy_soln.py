import os
import numpy as np
import itertools as it

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
print(list(it.combinations(arr, 2)))

test_word_list = ["slear", "nrash", "realt", "crane"]
test_comb = np.array([0,1,2,0,1])
test_comb_d = [d[pattern] for pattern in test_comb]

def wordchecker(wordlist, test_word, pattern):
    # n.b. for loops won't run if number n (where pattern == n) isn't found
    output_d = {}
    for i in range(0,len(wordlist)):
        wordcheck = wordlist[i]
        if 0 in pattern:
            for item in np.where(pattern == 0)[0]:
                if test_word[item] not in wordcheck:
                    output_d[wordcheck] = True

                    if 1 in pattern:
                        # 0, 1
                        for item in np.where(pattern == 1)[0]:
                            if wordcheck[item] == test_word[item]:
                                output_d[wordcheck] = True

                                # 0, 1, 2
                                for item in np.where(pattern == 2)[0]:
                                    if wordcheck[item] == test_word[item]:
                                        output_d[wordcheck] = True
                                    else:
                                        output_d[wordcheck] = False
                            else:
                                output_d[wordcheck] = False
                    else:
                        # 0, 2
                        for item in np.where(pattern == 2)[0]:
                            if wordcheck[item] == test_word[item]:
                                output_d[wordcheck] = True
                            else:
                                output_d[wordcheck] = False

                else:
                    output_d[wordcheck] = False
        # check for 1 if no 0s found
        elif 1 in pattern:
            for item in np.where(pattern == 1)[0]:
                if test_word[item] in wordcheck:
                    output_d[wordcheck] = True

                    # 1, 2
                    for item in np.where(pattern == 2)[0]:
                        if wordcheck[item] == test_word[item]:
                            output_d[wordcheck] = True
                        else:
                            output_d[wordcheck] = False
                else:
                    output_d[wordcheck] = False

        # only 2s remaining (you guess the exact word)
        else:
            for item in np.where(pattern == 2)[0]:
                if wordcheck[item] == test_word[item]:
                    output_d[wordcheck] = True
                else:
                    output_d[wordcheck] = False
    return output_d

print(wordchecker(test_word_list, "crane", np.array([2,2,2,1,1])))

def find_prob_distribution(wordlist, word):
    px = []
    tot = len(pattern_combinations)
    for pattern in pattern_combinations:
        wordcheck_d = wordchecker(wordlist, word, pattern)
        num_true = sum(wordcheck_d.values())
        print(pattern)
        print(num_true)
        px += [num_true/tot]
    return np.array(px)
#prob_dist = find_prob_distribution(test_word_list, "crane")
#print(prob_dist)
