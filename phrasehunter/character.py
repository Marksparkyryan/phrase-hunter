# Create your Character class logic in here.

from phrasehunter.phrase import Phrase

class Character(Phrase):
    # help Phrase determine how individual character should display itself

    def __init__(self):
        self.characters = []
        super().__init__()

    def __str__(self):
        display_phrase = []
        for char in self.phrase:
            if char in self.characters:
                display_phrase.append(f"{char}")
            elif char == " ":
                display_phrase.append(" ")
            else:
                display_phrase.append("_")
        return "".join(display_phrase)



                
    





    
    

