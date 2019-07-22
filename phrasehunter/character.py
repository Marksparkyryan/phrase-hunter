
class Character:

    def __init__(self, char):
        self.original = char
        self.char_guessed = False

    def update_char_guessed(self, guess):
        if self.original == guess:
            self.char_guessed = True
    
    def clean_space(self):
        if self.original == " ":
            self.char_guessed = True
            
    def show_character(self):
        if self.char_guessed:
            return self.original
        else:
            return "_"



      



                
    





    
    

