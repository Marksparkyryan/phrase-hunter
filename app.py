from phrasehunter.game import Game

PHRASES = [
    "winter is coming",
    "a diamond in the rough",
    "a house divided against itself cannot stand",
    "back to basics",
    "all is fair in love and war",
    "better late than never",
    "home is where the heart is",
]

if __name__ == "__main__":
    while True:
        game = Game(PHRASES)
        game.start_game()
        again = input("Play again? y/n")
        if again == "n":
            break




