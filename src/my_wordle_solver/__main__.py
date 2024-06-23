import click
import numpy as np
import my_wordle_solver.solver as solver
import my_wordle_solver.entropy_soln as entropy_soln

@click.group()
def main():
    pass

@main.command()
def run_solver():
    """This script runs the interactive wordle solver."""
    # input initial guess word
    word1 = input("Initial word guess: ")

    # input initial pattern from guess
    string = input("What pattern? (separate with spaces): ")
    pattern = np.array(list(map(int, string.split(' '))))
    solver.run(word1, pattern)
    

@main.command()
@click.option('--test', help='word to find probabilty distribution for')
def entropy(test):
    """This script calculates the entropies associated with each word"""
    if test:
        entropy_soln.test_word(test)
    else:
        entropy_soln.run()
    

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
