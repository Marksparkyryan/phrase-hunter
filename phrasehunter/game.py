# Create your Game class logic in here.
import random

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
        while self.lives:
            print(Phrase.show_phrase(phrase))
            guess = input("Guess a character! ")
            phrase.char_in_phrase_guessed(guess)
            phrase.update_phrase_guessed()
            if phrase.phrase_guessed:
                print("You guessed it!")
                break
            
            
            


            
            








    


            



