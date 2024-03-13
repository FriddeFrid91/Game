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
        sum = 0  
        if result == 1:
            print("--------------------")
            print("Sorry, you got a 1. Your turn is over.")
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
