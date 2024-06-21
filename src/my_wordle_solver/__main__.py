import click
import numpy as np
from termcolor import colored
from my_wordle_solver.letter_freq import find_probable_words, letter_freq_suggestion, WORD_LIST


@click.command()
def run_solver():
    # input initial guess word
    word1 = input("Initial word guess: ")

    # input initial pattern from guess
    string = input("What pattern? (separate with spaces): ")
    pattern = np.array(list(map(int, string.split(' '))))

    # begin loop
    word = word1
    wordlist = WORD_LIST
    while np.sum(pattern) != 10:
        nextwordlist = find_probable_words(wordlist, word, pattern)
        # print(nextwordlist)

        actual_entropy = np.log2(1/(len(nextwordlist)/len(wordlist)))
        click.echo(colored(f"Actual entropy from guess: {actual_entropy}", "yellow"), color=True)

        wordlist = nextwordlist
        remaining_entropy = np.log2(len(nextwordlist))
        click.echo(colored(f"Remaining entropy: {remaining_entropy}", "yellow"), color=True)


        if remaining_entropy>2.5:
            test_word = letter_freq_suggestion(nextwordlist, word, pattern)
        else:
            test_word = nextwordlist[0]
        click.echo(colored(test_word, "green"), color=True)
        word = test_word
        string = input("What pattern? (separate with spaces): ")
        pattern = np.array(list(map(int, string.split(' '))))



def main():
    run_solver()
    pass

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
