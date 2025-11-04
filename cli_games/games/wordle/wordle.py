from ...lib.colors import Color
from .getList import getList
from .table import createTable
import random
import pickle
from termgraph import Data, Args, BarChart # type: ignore
import click

@click.command(name="wordle")
@click.option("--chart", is_flag=True, help="Show a chart of your scores and exit.")
@click.option("--clear", is_flag=True, help="Clear scores and exit.")
def cmd(chart, clear):
    """
    Play the classic Wordle game in your terminal.

    \b
    You have 6 guesses to find the secret 5-letter word.
    Letters will turn:
      - Green if they are in the correct position
      - Yellow if they are in the word but in the wrong position
      - White if they are not in the word
    """

    def printState():
        print("\033c", end="")
        print(f"guess a five letter word in {GUESSES} guesses ")
        print("Remaining: " +  " ".join(POSSIBLE_LETTERS))
        print()
        createTable(GUESSES, ALL_GUESSES)
        print()

    def readScores():
        with open("cli_games/games/wordle/data.pkl", "rb") as f:
            data = pickle.load(f)
        return data
    
    def writeScores(data):
        with open("cli_games/games/wordle/data.pkl", "wb") as f:
            pickle.dump(data, f)

    def clearScores():
        data = [[0], [0], [0], [0], [0], [0], [0]]
        with open("cli_games/games/wordle/data.pkl", "wb") as f:
            pickle.dump(data, f)

    def updateScores(numberOfGuesses):
        scores = readScores()
        scores[numberOfGuesses][0] += 1
        writeScores(scores)

    if chart:
        scores = Data(readScores(), ["X", "1", "2", "3", "4", "5", "6"])
        args = Args(
            title="Scores",
            width=50,
            format="{:.0f}"
        )
        chartToShow = BarChart(scores, args)
        chartToShow.draw()
        return

    if clear:
        clearScores()
        return    
    
    possible_answers = getList("possible answers.json")
    valid_guesses = getList("both.json")
    ALL_GUESSES = []
    POSSIBLE_LETTERS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    GUESSES = 6
    VALID = True
    wordToGuess = random.choice(possible_answers)

    while len(ALL_GUESSES) < GUESSES:

        if VALID: printState()
        else: VALID = True
        inputText = input(">").lower()

        if inputText not in valid_guesses: 
            print(f"{Color.RED}invalid guess{Color.END}")
            VALID = False
            continue

        result_chars = [""] * len(inputText)
        remaining = {}
        for index, char in enumerate(wordToGuess):
            if inputText[index] == char:
                result_chars[index] = Color.GREEN + char + Color.END
            else:
                remaining[char] = remaining.get(char, 0) + 1

        for index, char in enumerate(inputText):
            if result_chars[index]:
                continue
            if remaining.get(char, 0) > 0:
                result_chars[index] = Color.YELLOW + char + Color.END
                remaining[char] -= 1
            else:
                result_chars[index] = char
        
        for char in inputText:
            if char in POSSIBLE_LETTERS:
                POSSIBLE_LETTERS.remove(char)

        ALL_GUESSES.append(result_chars)

        if inputText == wordToGuess:
            printState()
            print(Color.GREEN + "Congratulations, you guessed the word =)" + Color.END)
            updateScores(len(ALL_GUESSES))
            break

        if len(ALL_GUESSES) == GUESSES:
            printState()
            print(f"{Color.RED}You couldn't guess the word --> {wordToGuess}{Color.END}")
            updateScores(0)