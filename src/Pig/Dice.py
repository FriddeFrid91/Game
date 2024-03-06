import random


class Dice:
    """Class for the dice."""
    def __init__(self, numbers):
        self.numbers = numbers

<<<<<<< HEAD
    def rollTheDice(self):
        return random.randint(1, self.numbers)

    def showDiceRolls(self, rolls, rollTheDice):
        result = 0
        for _ in range(rolls):
            result += rollTheDice()
        return result
    
=======
    def rollTheDice(self, result):
        return random.randint(1, self.numbers)  
    
    def showTheDice(self, result, listOfPoints):
        if result == 1:
            print("Sorry, you got a 1. Your turn is over.")
            listOfPoints.clear()
            return 0
        else:
            print(f"You got a {result}!")
            return result
        
    def getDice(self):
        return self.numbers
    
    def setDice(self, numbers):
        self.numbers = numbers
    
    def __str__(self):
        return f"The dice has {self.numbers} sides."
>>>>>>> FriddeFrid_branch
