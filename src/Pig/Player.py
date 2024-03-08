<<<<<<< HEAD
"""Class for creating a player."""

import random
from Dice import Dice

class Player:
    """Class for creating a player."""

    def __init__(self, name):

        self.scores = 0
        self.dice = Dice(6)
        self.name = name
        self.numbers = self.dice.getDice()
        
    def player_move(self):
        """Player move."""
        roundScore = 0
        while roundScore < 100:
            roll = Dice.rollTheDice(self)
            print(f"You rolled a {roll}. Total score: {roundScore + roll}")
            roundScore += roll
    

            if roll == 1:
                roundScore = 0
                print(f"You rolled a 1. Total score: {roundScore}")
                break
           
            if roundScore >= 100:
                print(f"{playerNames} wins!")
                break

    def changeName(self, name):
        self.name = name
        return self.name
=======
class Player:
    """Class for creating a player."""
    def __init__(self, name, score):
        self.name = name
        self.score = score
>>>>>>> c65fa58fbfc7384a5fcdc3969564bf333c76ebb0

    def __str__(self):
        return f"{self.name} has {self.score} points."
  
    def get_name(self):
        """Get the name of the player."""
        return self.name
   
    def set_name(self, name):
        """Set the name of the player."""
        self.name = name

    def get_score(self):
        """Get the score of the player."""
        return self.score
<<<<<<< HEAD
    
    def changeName(self, name):
        self.name = name
        return self.name
   
    def getName(self):
        return self.name
   
    def getScores(self):
        return self.scores
    
    def setScores(self, scores):
        self.scores = scores
        return self.scores
    
    def setName(self, name):
        self.name = name
        return self.name    
=======

    def set_score(self, score):
        """Set the score of the player."""
        self.score = score

    def update_score(self, score):
        """Update the score of the player."""
        self.score += score
   
    def reset_score(self):
        """Reset the score of the player."""
        self.score = 0

    def add_score(self, score):
        """Add the score of the player."""
        self.score += score 
>>>>>>> c65fa58fbfc7384a5fcdc3969564bf333c76ebb0
