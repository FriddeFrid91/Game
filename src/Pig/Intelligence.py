<<<<<<< HEAD
"""This module contains the class for the intelligence."""
from Dice import Dice
"""This module contains the class for the intelligence."""
=======
import random
from Dice import Dice

class Intelligence:
    """Intelligence class"""
    def __init__(self):
        self.score = 0
>>>>>>> 0a2f121030da65ce5ced26eb046c9d2e04e98794

# Class for the intelligence


class Intelligence:
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
            roll = Dice.rollTheDice(self)
            print(f"Intelligence rolled a {roll}. Total score: {roundScore}")
            rollagain = Dice.rollTheDice(self)
            if roll == 1:
                roundScore = 0
                print(f"Intelligence rolled a 1. Total score: {roundScore}")
                print
            roundScore += roll
            if roundScore >= 100:
                print("Intelligence wins!")
                break

    def move(self):
        """Player move."""
        player = input("Enter your name: ")
        roundScore = 0
        while roundScore < 100:
            roll = Dice.rollTheDice(self)
            print(f"You rolled a {roll}. Total score: {roundScore}")
            if roll == 1:
                roundScore = 0
                print(f"You rolled a 1. Total score: {roundScore}")
            roundScore += roll
            if roundScore >= 100:
                print(f"{player} wins!")
                break
