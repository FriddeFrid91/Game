
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

    def load_testing(self):
        """Load the HighScore."""
        print(">> Highscore <<\n")
        with open(self.filename, "rb") as file:
            self.dict_of_highscores = pickle.load(file)
            print(f"{self.dict_of_highscores} testing OK")

    def save_testing(self, winner):
        """Save the high score."""
        if winner is None:
            return
        if winner in self.dict_of_highscores:
            self.dict_of_highscores[winner] += 1
        else:
            self.dict_of_highscores[winner] = 1

        with open(self.filename, "wb") as file:
            pickle.dump(self.dict_of_highscores, file)
        print(f"{self.dict_of_highscores} testing OK")

        return winner == ""
