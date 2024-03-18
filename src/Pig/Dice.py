import random


class Dice:
    """Class for the dice."""
    def __init__(self, numbers):
        self.rollTheDice = 0
        self.numbers = numbers

<<<<<<< HEAD
    def rollTheDice(self, result):
        return random.randint(1, self.numbers)  
    
    def showTheDice(self, result, listOfPoints):
=======
    def roll_the_dice(self):
        """Roll the dice. Return a random number between 1-6."""
        return random.randint(1, self.numbers)

    def show_the_dice(self, result):
        """Show the dices outcome."""
        sum = 0  
>>>>>>> main
        if result == 1:
            print("Sorry, you got a 1. Your turn is over.")
<<<<<<< HEAD
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
=======
            print("--------------------")
            return sum
        
        if result != 1:
            sum = result
            print("--------------------")
            print(f"You got a {result}!")
            print("--------------------")
            return sum   
        return sum

    def get_dice(self):
        """Get the number of sides of the dice."""
        return self.numbers
>>>>>>> main
