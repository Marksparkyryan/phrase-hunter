import os

from phrasehunter.game import Game

PHRASES = [
    "winter is coming",
    "a diamond in the rough",
    "a house divided against itself cannot stand",
    "back to basics",
    "all is fair in love and war",
    "better late than never",
    "home is where the heart is",
    "a bird in the 1 hand is worth 2 in the bush",
    "a dime a dozen",
    "piece of cake",
    "burst your bubble",
    "close but no cigar",
    "birds of 1 feather flock together",
    "practice makes perfect",
]

if __name__ == "__main__":
    while True:
        game = Game(PHRASES)
        game.start_game()
        again = input("Play again? [y/n] ")
        if again == "n":
            os.system("cls" if os.name == "nt" else "clear")
            print("Thanks for playing!", "\n")
            exit()
            