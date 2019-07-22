import random
import re
import os

from .phrase import Phrase
from .character import Character


class Game:
    """Game class will choose a random phrase from passed in phrases, 
    initialize user lives, and track previously guessed characters, 
    validate user guesses, and hold game loop logic. Game class will also 
    iterate over random phrase and turn each character into Chracter 
    object. Game class will check
    """
    def __init__(self, phrases):
        self.phrases = phrases
        self.current_phrase = random.choice(phrases)
        self.lives = 5
        self.already_guessed = []

    def create_char_objects(self):
        """Iterate over random phrase and turn each character into a 
        Chracter object then store objects as colection.
        """
        char_in_phrase_list = []
        for char in self.current_phrase:
            char_instance = Character(char)
            char_instance.clean_space()
            char_in_phrase_list.append(char_instance)
        return char_in_phrase_list
    
    def check_guess(self, phrase):
        """Validate user guesses by allowing only single letters a-z.
        """
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            try:
                print(f"You have {self.lives} lives remaining.")
                print("")
                print(Phrase.show_phrase(phrase))
                guess = str(input("Guess a letter [or 0 to quit]! > ")).lower()
                os.system("cls" if os.name == "nt" else "clear")
                if guess == "0":
                    print("Thanks for playing!", "\n")
                    exit()
                if re.match(r"^$", guess):
                    raise ValueError(f""""blank space" is not a valid letter!""")
                if re.match("^[a-z]$", guess) == None:
                    raise ValueError(f""""{guess}" is not a valid letter!""")
                if guess in self.already_guessed:
                    raise ValueError(f"""You've already guessed the letter "{guess}"!""")
            except ValueError as err:
                print(err)
            else:
                self.already_guessed.append(guess)
                return guess         


    def start_game(self):
        """Call on the creation of Character objects for each character 
        in phrase, then initialize a phrase object from a collection of 
        those Character objects, then prompt users for guesses while 
        lives are greater than 0.
        """
        phrase = Phrase(self.create_char_objects())
        
        while self.lives:
            guess = self.check_guess(phrase)     
            result = phrase.char_in_phrase_guessed(guess)
            if not result:
                self.lives -= 1
            phrase.update_phrase_guessed()
            if phrase.phrase_guessed:
                print(f"{phrase.show_phrase()}! You guessed it!", "\n")
                break
        print("Game over! You've run out of lives.", "\n")
            