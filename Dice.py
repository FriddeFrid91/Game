import random


class Dice:
    def __init__(self, numbers):
        self.numbers = numbers

    def rollTheDice(self):
        return random.randint(1, self.numbers)
    
    def showDiceRolls(dice, num_rolls):
        for _ in range(num_rolls):
            print(dice.rollTheDice())