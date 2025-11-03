import click
from .games.wordle import wordle
from .games.coin import coin

@click.group()
@click.version_option("1.0")
def main():
    """CLI games collection"""
    pass

main.add_command(wordle.cmd)
main.add_command(coin.cmd)

if __name__ == "__main__":
    main()