# Create your Character class logic in here.


class Character:
    # help Phrase determine how individual character should display itself

    def __init__(self, char):
        self.original = char
        self.char_guessed = False


    def update_char_guessed(self, guess):
        if self.original == guess or self.original == " ":
            self.char_guessed = True

    
    def show_character(self):
        if self.char_guessed or self.original == " ":
            return self.original
        else:
            return "_"



      



                
    





    
    

