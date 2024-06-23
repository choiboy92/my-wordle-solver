# my-wordle-solver

A python script to solve Wordle challenges using a mixture of information entropy and letter frequency analysis to determine the best next guess.
The script works by inputting the results from the first initial guess carried out by the user for the day's Wordle and suggests the best guess for the next attempt.

### Setup with Poetry
Make sure you have Poetry installed and download the required dependencies:
```shell
poetry install
```

### Usage
```
Usage: my-wordle-solver [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  entropy     This script calculates the entropies associated with each word
  run-solver  This script runs the interactive wordle solver.
```

### Running the script
1. To begin the script, run the command for the script:
```shell
poetry run my-wordle-solver run-solver
```
2. Input the initial word guess

3. Input the results of the initial guess - the user should input a series of space-separated numbers that indicate the results
> - **0** - ⬜️ - no matching letters
> - **1** - 🟨 - letter exists but not in correct place
> - **2** - 🟩 - letter exists and is in correct place
> 
> e.g. `0 0 1 0 2` corresponds to `⬜️⬜️🟨⬜️🟩` result pattern

4. The script should output a "best next guess" based on the previous guess, result pattern and entropy of remaining words

5. Repeat and continue till you get `🟩🟩🟩🟩🟩`


## How it works (the maths)
Coming soon...


