import random
import re
import time
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
        self.current_phrase = None
        self.lives = 5
        self.already_guessed = []
    
    def random_phrase(self):
        self.current_phrase = random.choice(self.phrases)

    def reset_attrs(self):
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
    
    def validate_phrase(self, phrase):  
        """Method checks for invalid characters in randomly selected 
        phrase. If invalid character is found, new phrase is selected 
        from PHRASES collection in app.py. If phrase is valid, phrase is 
        not changed. 
        """  
        for char in phrase:
            try:
                if re.match("^[a-z ]$", char) == None:
                    raise ValueError(f""""{self.current_phrase}" contains"""
                    f""" an invalid character "{char}"! Please modify/remove"""
                    """ this phrase in PHRASES.""")
            except ValueError as err:
                for i in range(5):
                    os.system("cls" if os.name == "nt" else "clear")
                    print(err)
                    print("Selecting new phrase", "." * i, sep="")
                    time.sleep(1)
                self.random_phrase()
                self.validate_phrase(self.current_phrase)
                
    def validate_guess(self, char, phrase):
        """Method checks for invalid characters in user's guess and 
        tracks/prevents characters that have already been guessed.
        """                    
        while True:
            try:
                if char == "0":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Thanks for playing!", "\n")
                    exit()
                if re.match(r"^$", char):
                    raise ValueError(f""""nothing" is not a valid letter!""")
                if re.match("^[a-z]$", char) == None:
                    raise ValueError(f""""{char}" is not a valid letter!""")
                if char in self.already_guessed:
                    raise ValueError(f""""{char}" has alrady been entered!""")
            except ValueError as err:
                os.system("cls" if os.name == "nt" else "clear")
                print(err)
                print(f"You have {self.lives} lives remaining.", "\n")
                print(Phrase.show_phrase(phrase))
                char = str(input("Guess a letter or [0 to quit] > ")).lower()
                continue
            else:
                self.already_guessed.append(char)
                return char

    def start_game(self):
        """Establish a valid phrase, prompt for valid guesses against that 
        phrase, track user lives, and monitor if phrase has been guessed.   
        """
        self.random_phrase()
        self.validate_phrase(self.current_phrase)
        phrase = Phrase(self.create_char_objects())
        
        while self.lives:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"You have {self.lives} lives remaining.", "\n")
            print(Phrase.show_phrase(phrase))
            guess = str(input("Guess a letter or [0 to quit] > ")).lower()
            valid = self.validate_guess(guess, phrase)  
            result = phrase.char_in_phrase_guessed(valid)
            if not result:
                self.lives -= 1
                if self.lives == 0:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Game over! You've run out of lives.", "\n")
                    break
            phrase.update_phrase_guessed()
            if phrase.phrase_guessed:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{phrase.show_phrase()}! You guessed it!", "\n")  
                break
            