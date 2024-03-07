"""Class for creating a player."""


class Player:
    """Class for creating a player."""
    def __init__(self, name):
        self.name = name
        self.scores = 0

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
