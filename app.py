# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop

from phrasehunter.game import Game

if __name__ == "__main__":
    while True:
        inst = Game()
        inst.start_game()
        again = input("Play again? y/n")
        if again == "n":
            break




