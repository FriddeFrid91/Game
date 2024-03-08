"""This module contains the class for the intelligence."""
import random
from Dice import Dice
from Player import Player

"""This module contains the class for the intelligence."""

# Class for the intelligence


class Intelligence():
    """Intelligence class."""

    def __init__(self):
        """Create the intelligence with a score and a dice."""
        self.score = 0
        self.dice = Dice(6)
        self.numbers = self.dice.getDice()

    def intelligence_move(self):
        """Intelligence move."""
        roundScore = 0
        while roundScore < 100:
<<<<<<< HEAD
            roll = Dice.roll_the_dice(self)
            print(f"Intelligence rolled a {roll}. Total score: {roundScore}")  
=======
            roll = Dice.rollTheDice(self)
            print(f"Intelligence rolled a {roll}. Total score: {roundScore + roll}")
>>>>>>> 45f3de2e083709629479938239cb8db8acd05c0a
            roundScore += roll
            
            if roll == 1:
                roundScore = 0
                print(f"Intelligence rolled a 1. Total score: {roundScore}")
                break
           
            if roundScore >= 100:
                print("Intelligence wins!")
                break



        

 
