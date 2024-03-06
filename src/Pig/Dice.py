import random


class Dice:
    def __init__(self, numbers):
        self.numbers = numbers

<<<<<<< HEAD
    def rollTheDice(self):
        return random.randint(1, self.numbers)

    def showDiceRolls(self, rolls, rollTheDice):
        result = 0
        for a in range(rolls):
            result += rollTheDice()
        return result
=======
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
>>>>>>> ae413fbad387d7a3b39b3fa704cb0442a3fdc55b
