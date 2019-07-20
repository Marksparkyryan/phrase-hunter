# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop

from phrasehunter.game import Game

PHRASES = [
    "winter is coming",
    "one small step for man, one giant leap for mankind",
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




