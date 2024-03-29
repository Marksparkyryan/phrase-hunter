import os
import re
import time

class Character:
    """Character class will receive one character, initialize an instance based on 
    that character, and display that character in its original form or 
    redact it with an underscore character. 
    """
    def __init__(self, char):
        self.original = char
        self.char_guessed = False

    def update_char_guessed(self, guess):
        """If guess matches original character, change char_guessed 
        to True 
        """
        if self.original == guess:
            self.char_guessed = True
    
    def clean_space(self):
        """If original character is a space, change char_guessed to True. 
        Not revealing space characters would make game too difficult.
        """
        if self.original == " ":
            self.char_guessed = True
            
    def show_character(self):
        """If the character has been guessed by the user, display the 
        orginal form of the character. Else, display the character as an 
        underscore (hide the character).
        """
        if self.char_guessed:
            return self.original
        else:
            return "_"
    
    @classmethod
    def create_character(cls, char):
        """Classmethod will validate passed in character (only letters 
        a-z and spaces are permitted). If valid, character is instantiated.
        """
        try:
            if re.match("^[a-z ]$", char) == None:
                raise ValueError("Character Error: Only letters a-z and "
                "spaces are permitted in phrase.")
        except ValueError as err:
                print(err)
                time.sleep(2)
                return False
        else:
            return cls(char)
