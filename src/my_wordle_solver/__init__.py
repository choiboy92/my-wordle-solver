__version__ = "0.1.0"

WORD_LIST = []

with open('data/possible_words.txt') as f:
    for word in f.readlines():
        WORD_LIST += [word.strip()]
