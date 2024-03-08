"""This module contains the class for the dice."""
import random
"""This module contains the class for the dice."""

# Class for the dice


class Dice:
    """Class for the dice."""

    def __init__(self, numbers):
        """Create the dice with the number of sides."""
        self.numbers = numbers

    def roll_the_dice(self):
        """Roll the dice. Return a random number between 1-6."""
        return random.randint(1, self.numbers)

    def show_the_dice(self, result):
        """Show the dices outcome."""
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
        """Get the number of sides on the dice."""
        return self.numbers

    def setDice(self, numbers):
        """Set the number of sides on the dice."""
        self.numbers = numbers

    def __str__(self):
        """Return the number of sides on the dice."""
        return f"The dice has {self.numbers} sides."
