
"""The HighScore class. Contains the high score logic for the game of Pig."""
import pickle


class HighScore:
    """The HighScore class. Contains the high score logic for the game of Pig."""

    def __init__(self):
        """Create the high score."""
        self.scores = {}

    def saveScore(self, dictOfScores):
        """Save the high score to a file."""
        highScoreDict = dictOfScores
        player1, player2 = list(highScoreDict.keys())
        score1, score2 = list(highScoreDict.values())
        print(player1, player2, score1, score2)
        currentWins = 0
        currentLosses = 0

        if score1 > score2:
            winner = player1
            loser = player2
            currentWins += 1
            currentLosses += 1
        elif score1 < score2:
            winner = player2
            loser = player1
            currentWins += 1
            currentLosses += 1

        updatedScores = {winner: currentWins, loser: currentLosses}
        print(updatedScores)
    
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
