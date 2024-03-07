
"""The HighScore class. Contains the high score logic for the game of Pig."""
import pickle


class HighScore:
    """The HighScore class. Contains the high score logic for the game of Pig."""

    def __init__(self):
        """Create the high score."""
        self.scores = {}

    def saveScore(self, dictOfScores):
        """Save the high score to a file."""
        self.scores.update(dictOfScores)
        with open("highscore.bin", "ab") as file:
            pickle.dump(self.scores, file)

    def loadScore(self):
        """Load the high score from a file."""
        try:
            with open("highscore.bin", "rb") as file:
                scores = pickle.load(file)
            for key, value in self.scores.items():
                print(f"{key} got {value} points.")
            return scores
        except FileNotFoundError:
            print("No high score found.")
            self.scores = {}
