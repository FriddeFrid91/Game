"""Class for creating a player."""


class Player:
 
    def __init__(self, name):
        self.name = name
        self.score = 0

    def createPlayer(self, name):
        self.name = name
        self.score = 0 
        return "Player added: " + self.name, self.score
    
    def addPoints(self, points):
        self.score += points
        return self.score
    
    def changeName(self, name):
        self.name = name
        return self.name
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        return self.name    
