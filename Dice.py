import random

class Dice:
    def __init__(self, numbers):
        self.numbers = numbers

    def rollTheDice(self):
        return random.randint(1, self.numbers)

    def showDiceRolls(self, rolls, rollTheDice):
        result = 0
        for a in range(rolls):
            result += rollTheDice()
        return result
