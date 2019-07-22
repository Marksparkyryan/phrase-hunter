import random

from .character import Character


class Phrase:
    """Phrase class will receive a collection of Character objects as 
    phrase, check if the phrase has been guessed, and display the phrase b
    ased on each Characters guessed state.
    """
    def __init__(self, phrase):
        self.char_in_phrase_list = phrase
        self.phrase_guessed = False     
    
    def char_in_phrase_guessed(self, guess):
        """Will receive user's guess, iterate through un-guessed 
        characters, and locate matches if any and change that Chracter's 
        guessed state.
        """
        char_guessed = False
        for char in self.char_in_phrase_list:
            if not char.char_guessed:
                char.update_char_guessed(guess)
                if char.char_guessed:
                    char_guessed = True
        return char_guessed

    def update_phrase_guessed(self):
        """Determine length of phrase as count, decrement count by 1 for 
        each successful guessed character in phrase, if count reaches 0 
        then phrase is guessed.
        """
        count = len(self.char_in_phrase_list)
        for char in self.char_in_phrase_list:
            if char.char_guessed == True:
                count -= 1
        if count == 0:
            self.phrase_guessed = True  

    def show_phrase(self):
        """Iterate through Character objects, display them based on their 
        guessed state, then join them into a string representing the phrase.
        """
        phrase = []
        for char in self.char_in_phrase_list:
            phrase.append(Character.show_character(char))
        string_phrase = "".join(phrase)
        return string_phrase.capitalize()
