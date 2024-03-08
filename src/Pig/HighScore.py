
"""The HighScore class. Contains the high score logic for the game of Pig."""
import pickle


class HighScore:
    """The HighScore class. Contains the high score logic."""

    def __init__(self):
        """Create the high score."""
        self.dict_of_highscores = {}
        self.filename = "highscore.txt"

    def __str__(self):
        """Return the high score."""
        return f"High score: {self.filename} "
    
    def save_score(self, winner):
        """Save the high score."""
        new_dict = {winner: 1}
        print(new_dict)

    def get_highScore(self):
        """Get the high score."""
        for a in self.dict_of_highscores:
            return f"{a} has {self.dict_of_highscores[a]} wins."
