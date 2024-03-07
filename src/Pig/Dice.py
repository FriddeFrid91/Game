import random

class Dice:
    """Class for the dice."""
    def __init__(self, numbers):
        self.numbers = numbers

    def rollTheDice(self):
        return random.randint(1, self.numbers)

    def showTheDice(self, result):
        if result == 1:
            print("--------------------")
            print("Sorry, you got a 1. Your turn is over.")
            print("--------------------")
            return 0
        else:
            print("--------------------")
            print(f"You got a {result}!")
            print("--------------------")
            return result
        
    def getDice(self):
        return self.numbers
    
    def setDice(self, numbers):
        self.numbers = numbers
    
    def __str__(self):
        return f"The dice has {self.numbers} sides."

