import click
import random
from cli_games.lib.colors import Color

@click.command(name="coin")
@click.argument("number", required=False)
def cmd(number):
    """
    Flip a coin in your terminal.

    \b
    You can either flip once or specify how many times to flip.
    For multiple flips, it will show how many times each side appeared.

    \b
    Examples:
      cli-games coin        → flips once
      cli-games coin 10     → flips 10 times and shows totals
    """

    COIN = ["heads", "tails"]
    
    flipCounter = {"heads": 0, "tails": 0}
    try:
        number = int(number)
        for x in range(number):
            coinFlip = random.choice(COIN)
            flipCounter[coinFlip] += 1
        
        print(f"{Color.BOLD}Coin Flip Results ({number} flips):{Color.END}")
        print(f"  {Color.PURPLE}Heads:{Color.END} {flipCounter['heads']}")
        print(f"  {Color.CYAN}Tails:{Color.END} {flipCounter['tails']}")

        if flipCounter["heads"] > flipCounter["tails"]:
            print(f"{Color.GREEN}Heads wins!{Color.END}")
        elif flipCounter["tails"] > flipCounter["heads"]:
            print(f"{Color.GREEN}Tails wins!{Color.END}")
        else:
            print(f"{Color.BLUE}It's a tie!{Color.END}")
        
    except:
        print(Color.PURPLE + "The coin flipped " + Color.BOLD + random.choice(COIN) + Color.END) 