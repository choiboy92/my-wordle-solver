import numpy as np
from scipy import stats
import json
from utilities.common import WORD_LIST, PATTERN_COMBINATIONS
import utilities.common

# NUMBERS TO PATTERN TRANSLATION
# d = {0: "NO", 1: "IN-WORD", 2: "EXACT"}

def patternmatch(wordcheck, test_word, pattern):
    equalmat = np.zeros(5)
    checkmat = np.zeros(5)

    # check 2s (you guess the exact word)
    for item in np.where(pattern == 2)[0]:
        if test_word[item] == wordcheck[item]:
            equalmat[item] = 1
            checkmat[item] = 1
        else:
            return False

    # check for 1s
    for item in np.where(pattern == 1)[0]:  #2, 3, 4 (e, e, d)
        if test_word[item] in wordcheck and test_word[item]!=wordcheck[item]:
            ind = wordcheck.index(test_word[item])

            if checkmat[ind] ==0:
                checkmat[ind] =1
                equalmat[item] = 1
            elif len(utilities.common.find(wordcheck, test_word[item]))>1:
                checkmat[wordcheck.index(test_word[item], ind +1)] =1
                equalmat[item] = 1
            else:
                return False
        else:
            return False

    # check for 0s
    for item in np.where(pattern == 0)[0]:
        if test_word[item] not in wordcheck:
            equalmat[item] = 1
        else:   #if letter in wordcheck
            #check first instance of letter has been checked already
            if checkmat[wordcheck.index(test_word[item])] == 1 and wordcheck.count(test_word[item])<2:
                equalmat[item] = 1
            else:
                return False
    if np.sum(equalmat) == 5:
        return True

def wordchecker(wordlist, test_word, pattern):
    # n.b. for loops won't run if number n (where pattern == n) isn't found
    output_d = {}
    for i in range(0,len(wordlist)):
        output_d[wordlist[i]] = patternmatch(wordlist[i], test_word, pattern)
    return output_d



def find_prob_distribution(wordlist, word):
    px = []
    tot = float(len(wordlist))
    for pattern in PATTERN_COMBINATIONS:
        wordcheck_d = wordchecker(wordlist, word, pattern)
        num_true = sum(wordcheck_d.values())
        px += [num_true/tot]
        #print(tot)
    return np.array(px)


def create_entropy_data(possible_words):
    ent = {}
    for word in possible_words:
        prob_dist = find_prob_distribution(WORD_LIST, word)
        ent[word] = stats.entropy(prob_dist, base=2)
    with open('word_entropy_initial.json', 'w+') as f:
        # this would place the entire output on one line
        # use json.dump(ent, f, indent=4) to "pretty-print" with four spaces per indent
        json.dump(ent, f, indent=4)
    return ent

#ent_1 = create_entropy_data(WORD_LIST)

# test_word_list = ["steal", "crepe", "erase", "abide", "irate"]
# test_comb = np.array([0,1,2,0,1])
# test_comb_d = [d[pattern] for pattern in test_comb]

#print(wordchecker(test_word_list, "crane", np.array([1,1,1,1,1])))

prob_dist = find_prob_distribution(WORD_LIST, "stare")
print(prob_dist)
print(stats.entropy(prob_dist))