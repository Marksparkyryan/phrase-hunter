import os

from phrasehunter.game import Game

PHRASES = [
    "1winter is coming",
    "a diamond in the rough",
    "a house divided against itself cannot stand",
    "back to basics",
    "1all is fair in love and war",
    "1better late than never",
    "1home is where the heart is",
    "a bird in the hand is worth two in the bush",
    "a dime a dozen",
    "piece of cake",
    "1burst your bubble",
    "1close but no cigar",
    "1birds of a feather flock together",
    "1practice makes perfect",
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
            