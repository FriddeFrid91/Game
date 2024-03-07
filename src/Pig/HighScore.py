
"""The HighScore class. Contains the high score logic for the game of Pig."""
import pickle


class HighScore:
    """The HighScore class. Contains the high score logic for the game of Pig."""

    def __init__(self):
        """Create the high score."""
        self.scores = {}

    def saveScore(self, dictOfScores):
        """Save the high score to a file."""
        dictOfScores.update(self.scores)
        print(f"TESSSST {self.scores}")
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
            self.scores = {}
