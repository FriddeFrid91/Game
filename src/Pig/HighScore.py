
"""The HighScore class. Contains the high score logic for the game of Pig."""
import pickle

# Class to store the high score
class HighScore:
    def __init__(self):
        self.score = 0

    def saveScore(self):
        with open("highscore.txt", "wb") as file:
            pickle.dump(self.score, file)

    def loadScore(self):
        try:
            with open("highscore.txt", "rb") as file:
                self.score = pickle.load(file)
        except FileNotFoundError:
            print("No high score found. Starting a new game.")
            self.score = 0

    def showHighScore(self):
        print(f"The current high score is: {self.score}")

    def updateHighScore(self, score):
        if score > self.score:
            self.score = score
            print("Congratulations! You have a new high score!")
            self.saveScore()
        else:
            print("You did not beat the high score this time.")

    def addScore(self, score):
        self.score += score

    def getScore(self):
        return self.score

    def resetScore(self):
        self.score = 0
