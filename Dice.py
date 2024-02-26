class Dice:

    def __init__(self, dice):
        self.dice = dice

    def throwDice(self, resultOfDice):
        if resultOfDice == 1:
            return ("Sorry! You got a 1.")
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
