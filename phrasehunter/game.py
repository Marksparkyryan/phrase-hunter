# Create your Game class logic in here.
import random
import re

from .phrase import Phrase
from .character import Character


class Game:

    def __init__(self, phrases):
        self.phrases = phrases
        self.current_phrase = random.choice(phrases)
        self.lives = 5

    def create_char_objects(self):
        char_in_phrase_list = []
        for char in self.current_phrase:
            char_instance = Character(char)
            char_in_phrase_list.append(char_instance)
        return char_in_phrase_list

    def start_game(self):
        phrase = Phrase(self.create_char_objects())
        already_guessed = []
        
        while self.lives:
            try:
                print("")
                print(Phrase.show_phrase(phrase))
                guess = str(input(f"You have {self.lives} lives remaining. Guess a letter! > ")).lower()
                if re.match("^[a-z]$", guess) == None:
                    raise ValueError(f"{guess} is not a valid letter!")
                if guess in already_guessed:
                    raise ValueError(f"You've already guessed the letter {guess}!")
            except ValueError as err:
                print(err)
            
            else:
                already_guessed.append(guess)      
                result = phrase.char_in_phrase_guessed(guess)
                if not result:
                    self.lives -= 1
                phrase.update_phrase_guessed()
                if phrase.phrase_guessed:
                    print("You guessed it!")
                    break
            
            
            


            
            








    


            



