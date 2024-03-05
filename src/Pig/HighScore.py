class HighScore:
    def __init__(self):
        self.score = 0
    def addScore(self, score):
        self.score += score
    def getScore(self):
        return self.score
    def resetScore(self):
        self.score = 0