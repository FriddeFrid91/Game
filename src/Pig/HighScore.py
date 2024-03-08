
"""The HighScore class. Contains the high score logic for the game of Pig."""
import pickle
from Game import Game


class HighScore:
    """The HighScore class. Contains the high score logic."""

    def __init__(self):
        """Create the high score."""
        self.scores = {}
        super().__init__()
        Game.__init__(self)

    def saveScore(self, dictOfScores):
        """Save the high score to a file."""
        highScoreDict = dictOfScores
        player1, player2 = list(highScoreDict.keys())
        score1, score2 = list(highScoreDict.values())
        print(player1, player2, score1, score2)
 
        if score1 > score2:
            winner = player1
            loser = player2

        elif score1 < score2:
            winner = player2
            loser = player1
        win = self.scores.setdefault(winner, {'wins': 0, 'losses': 0})['wins']
        win += 1
        loss = self.scores.setdefault(loser, {'wins': 0, 'losses': 0})['losses']
        loss += 1

        updated_Scores = {winner: win, loser: loss}
        self.scores.update(updated_Scores)
        print(updated_Scores)

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
