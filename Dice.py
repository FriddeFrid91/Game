class Dice:

    def __init__(self, dice):
        self.dice = dice

    def throwDice(self, resultOfDice):
        if resultOfDice == 1:
            return ("Oh no, you got a 1. You get 0 points from this round.")
        if resultOfDice == 2:
            return ("You got a 2!")
        if resultOfDice == 3:
            return ("You got a 3!")
        if resultOfDice == 4:
            return ("You got a 4!")
        if resultOfDice == 5:
            return ("You got a 5!")
        if resultOfDice == 6:
            return ("You got a 6!")
