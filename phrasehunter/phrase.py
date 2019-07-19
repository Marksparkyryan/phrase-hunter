import random

from phrasehunter.character import Character

class Phrase:
    def __init__(self, phrase):
        self.char_in_phrase_list = phrase
        self.phrase_guessed = False     
    
    def char_in_phrase_guessed(self, guess):
        for char in self.char_in_phrase_list:
            char.update_char_guessed(guess)

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
    
    def __str__(self):
        pass








    
    
    



        




        
    



    