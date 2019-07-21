import random
import re
import os

from .phrase import Phrase
from .character import Character


class Game:

    def __init__(self, phrases):
        self.phrases = phrases
        self.current_phrase = random.choice(phrases)
        self.lives = 5
        self.already_guessed = []

    def create_char_objects(self):
        char_in_phrase_list = []
        for char in self.current_phrase:
            char_instance = Character(char)
            char_instance.clean_space()
            char_in_phrase_list.append(char_instance)
        return char_in_phrase_list
    
    def check_guess(self, phrase):
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            try:
                print(f"You have {self.lives} lives remaining.")
                print("")
                print(Phrase.show_phrase(phrase))
                guess = str(input("Guess a letter! > ")).lower()
                os.system("cls" if os.name == "nt" else "clear")
                if guess == "0":
                    print("Thanks for playing!", "\n")
                    exit()
                if re.match(r"^$", guess):
                    raise ValueError(f""""blank space" is not a valid 
                    letter!""")
                if re.match("^[a-z]$", guess) == None:
                    raise ValueError(f""""{guess}" is not a valid letter!""")
                if guess in self.already_guessed:
                    raise ValueError(f"""You've already guessed the letter 
                    "{guess}"!""")
            except ValueError as err:
                print(err)
            else:
                self.already_guessed.append(guess)
                return guess         


    def start_game(self):
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
            
            
            
            
            


            
            








    


            



