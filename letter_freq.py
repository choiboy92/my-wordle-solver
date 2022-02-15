import numpy as np

WORD_LIST = []

with open('possible_words.txt') as f:
    for word in f.readlines():
        WORD_LIST += [word.strip()]

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

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
            elif len(find(wordcheck, test_word[item]))>1:
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


test_word = "crane"
test_pattern = np.array([2,2,2,0,0])
next_guess = [None, None, None, None, None]

# Find next possible wordlist from given word and pattern that arises
output_d = wordchecker(WORD_LIST, test_word, test_pattern)
next_wordlist = []
for word in output_d:
    if output_d[word] == True:
        next_wordlist += [word]
print(next_wordlist)

# Setup frequency database
def freq_setup():
    freq = {}
    for i in range(0, 26):
        freq[chr(ord('`')+i+1)] = np.zeros(5)
    return freq

def letter_freq_suggestion(wordlist):
    freq = freq_setup()

    for word in wordlist:
        for i in range(0,len(word)):
            freq[word[i]][i] = freq[word[i]][i] + 1
    # Only if initial guess gives us enough information
    if np.sum(test_pattern)>=2:

        for item in np.where(test_pattern == 2)[0]:
            next_guess[item] = test_word[item]

        for item in np.where(test_pattern == 1)[0]:
            ind = np.argmax(freq[test_word[item]])
            second_ind = freq[test_word[item]].argsort()[-2]
            # ensure frequency suggestion of letter isn't in same place as any green
            if ind != item and next_guess[ind] == None:
                next_guess[ind] = test_word[item]
            elif next_guess[second_ind]== None:
                next_guess[second_ind] = test_word[item]

        print(next_guess)
        # Find inidices where next_guess is NOT None
        l=[i for i,v in enumerate(next_guess) if v != None]
        available_words = []

        # Find words in wordlist that match the next guess estimate
        for word in wordlist:
            match = np.zeros(5)
            for n in l:
                if word[n] == next_guess[n]:
                    match[n] = 1
            if np.sum(match) == len(l):
                available_words += [word]
        # sort letter_freq suggestions by entropy
        print(available_words)
        return
    else:
        print("Not enough information")
        # Select next word based on information entropy
        return

letter_freq_suggestion(next_wordlist)
