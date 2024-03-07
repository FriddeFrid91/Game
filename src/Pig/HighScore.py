
"""The HighScore class. Contains the high score logic for the game of Pig."""
import pickle


class HighScore:
    """The HighScore class. Contains the high score logic for the game of Pig."""

    def __init__(self):
        """Create the high score."""
        self.scores = {}

    def saveScore(self, dictOfScores):
        """Save the high score to a file."""
        updatedScores = {}
        score1, score2 = dictOfScores.values()
        player1, player2 = dictOfScores.keys()

        print(score1, player1, score2, player2)
        if score1 > score2:
            updatedScores.update(player1)
            for key, value in updatedScores.items():
                print(f"{key} got {value} points.")
            print(f"Winner: {player1}")
            self.scores[player1] = score1
            updatedScores.update(player1)
        elif score1 < score2:
            print(f"Winner: {player2}")
            self.scores[player2] = score2
            updatedScores.update(self.scores)

        with open("highscore.bin", "ab") as file:
            pickle.dump(self.scores, file)

    def loadScore(self):
        """Load the high score from a file."""
        try:
            with open("highscore.bin", "rb") as file:
                pickle.load(file)
            for key, value in self.scores.items():
                print(f"{key} got {value} points.")
            return self.scores.items()
        except FileNotFoundError:
            print("No high score found.")
            self.scores = {}
