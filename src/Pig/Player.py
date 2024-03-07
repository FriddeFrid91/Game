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

    def __str__(self):
        return f"{self.name} has {self.scores} points."
    
    def addPoints(self, scores):
        self.score += scores
        return self.score
    
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
