"""Class for creating a player."""


class Player:
 
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return f"Player: {self.name} - Score: {self.score}"

    def createPlayer(self, name):
        self.name = name
        self.score = 0 
        return self.name, self.score
