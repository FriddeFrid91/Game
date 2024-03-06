class HighScore:
    def __init__(self):
        self.score = 0
    def addScore(self, score):
        self.score += score
    def getScore(self):
        return self.score
    def resetScore(self):
        self.score = 0
    def __str__(self):
        '''Return a string representation of the score'''
        return f"Highscore: {self.score}"
    