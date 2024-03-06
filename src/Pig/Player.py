class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def createPlayer(self, name):
        self.name = name
        self.score = 0  
        return self.name, self.score
    
    def showPlayer(self):
        print(f"Player: {self.name} - Score: {self.score}")
        return self.name, self.score
