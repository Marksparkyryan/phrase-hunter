import random

from .character import Character

class Phrase:
    def __init__(self, phrase):
        self.char_in_phrase_list = phrase
        self.phrase_guessed = False     
    
    def char_in_phrase_guessed(self, guess):
        char_guessed = False
        for char in self.char_in_phrase_list:
            if not char.char_guessed:
                char.update_char_guessed(guess)
                if char.char_guessed:
                    char_guessed = True
        return char_guessed

    def update_phrase_guessed(self):
        count = len(self.char_in_phrase_list)
        for char in self.char_in_phrase_list:
            if char.char_guessed == True:
                count -= 1
        if count == 0:
            self.phrase_guessed = True  

    def show_phrase(self):
        phrase = []
        for char in self.char_in_phrase_list:
            phrase.append(Character.show_character(char))
        return "".join(phrase)
    









    
    
    



        




        
    



    