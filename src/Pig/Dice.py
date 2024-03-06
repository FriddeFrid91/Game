import random


class Dice:
    def __init__(self, numbers):
        self.numbers = numbers

    def rollTheDice(self, result):
        if self.numbers == 1:
            return "Sorry"
        else:
            return random.randint(1, self.numbers)
    
    def getDice(self):
        return self.numbers
    
    def setDice(self, numbers):
        self.numbers = numbers
    
    def __str__(self):
        return f"The dice has {self.numbers} sides."
