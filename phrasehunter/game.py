# Create your Game class logic in here.
import re
import os

from phrasehunter.phrase import Phrase
from phrasehunter.character import Character


class Game:

    def __init__(self):
        self.round = Character()
        self.lives = 5
    
    def start_game(self):
        print(f"""\"{self.round}\"""")
        print("Guess a character!")
        while self.lives:
            try:
                guess = input(f"You have {self.lives} incorrect guesses left. guess another character! ").lower()
                if guess == "0":
                    break
                if guess in self.round.characters:
                    raise ValueError(f"""You already guessed the letter "{guess}"!""")
                if not re.search(r"^[a-z]{1}$", guess):
                    raise ValueError("You must guess a single letter!")
            except ValueError as err:
                print(err)
            else:
                self.round.characters.append(guess)
                if guess not in self.round.phrase:
                    self.lives -= 1
                self.clear_screen()
                print(f"""\"{self.round}\"""")
        print("You've lost! You've guessed incorrectly too many times!")
    
    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


            
    




