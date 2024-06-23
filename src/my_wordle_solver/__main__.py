import click
from my_wordle_solver.solver import run
import numpy as np


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
    run(word1, pattern)
    


@main.command()
def entropy():
    """This script calculates the entropies associated with each word"""
    import entropy_soln



if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
