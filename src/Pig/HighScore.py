
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
        if winner in self.dict_of_highscores:
            self.dict_of_highscores[winner] += 1
        else:
            self.dict_of_highscores[winner] = 1
        try:
            with open(self.filename, "wb") as file:
                pickle.dump(self.dict_of_highscores, file)
        except FileNotFoundError:
            print("File not found.")
 
    def load_score(self):
        """load the high score."""
        try:
            with open(self.filename, "rb") as file:
                self.dict_of_highscores = pickle.load(file)
        except FileNotFoundError:
            print("File not found.")
        return self.dict_of_highscores

    def get_highScore(self):
        """Get the high score."""
        for a in self.dict_of_highscores:
            return f"{a} has {self.dict_of_highscores[a]} wins."
