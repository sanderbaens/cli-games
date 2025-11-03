def createTable(amountOfGuesses:int, guesses:list):
    print("┌" + "───┬" * 4 + "───┐")
    for x in range(amountOfGuesses):
        if x < len(guesses):
            for letter in guesses[x]:
                print(f"│ {letter} ", end="")
            print("│")
        else:
            print("│   " * 5 + "│")
        if x + 1 < amountOfGuesses:
            print("├" + "───┼" * 4 + "───┤")
        else:
            print("└" + "───┴" * 4 + "───┘")