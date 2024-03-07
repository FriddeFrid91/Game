
"""The HighScore class. Contains the high score logic for the game of Pig."""
import pickle


class HighScore:
    """The HighScore class. Contains the high score logic for the game of Pig."""
 
    def __init__(self):
        """Create the high score."""
        self.score = 0

    def saveScore(self, dictOfScores):
        """Save the high score to a file."""
        for key, value in dictOfScores.items():
            print(key, value)
        print(f" TEST{dictOfScores}")
        with open("highscore.bin", "wb") as file:
            pickle.dump(dictOfScores, file)

    def loadScore(self):
        """Load the high score from a file."""
        try:
            with open("highscore.bin", "rb") as file:
                scores = pickle.load(file)
                return scores
        except FileNotFoundError:
            print("No high score found.")
            self.score = 0

    def addScore(self, score):
        self.score += score

    def getScore(self):
        return self.score

    def resetScore(self):
        self.score = 0
