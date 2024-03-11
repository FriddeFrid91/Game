
"""The HighScore class. Contains the high score logic for the game of Pig."""
import pickle
from Player import Player


class HighScore:
    """The HighScore class. Contains the high score logic."""

    def __init__(self):
        """Create the high score."""
        self.dict_of_highscores = {}
        self.player = Player(name="", score=0)
        self.filename = "highscore.txt"

    def __str__(self):
        """Return the high score."""
        return f"High score: {self.filename} "

    def load_score(self):
        """Load the HighScore."""
        print(">> Highscore <<\n")
        # Load the high score from the file.
        with open(self.filename, "rb") as file:
            self.dict_of_highscores = pickle.load(file)

        # Sorts the dictionary by value and reverses it.
        sorted_dict = {k: v for k, v in sorted(self.dict_of_highscores.items(),
                                               key=lambda item: item[1],
                                               reverse=True)}
        # Prints the sorted dictionary by key and value.
        for key, value in sorted_dict.items():
            print(f"{key} : {value}")

    def save_score(self, winner):
        """Save the high score."""
        # If winner is None, return.
        if winner is None:
            return
        # If winner is in the dictionary, add 1 to the value.
        if winner in self.dict_of_highscores:
            self.dict_of_highscores[winner] += 1
        # If winner is not in the dictionary, set the value to 1.
        else:
            self.dict_of_highscores[winner] = 1
        # Save the dictionary to the file.
        with open(self.filename, "wb") as file:
            pickle.dump(self.dict_of_highscores, file)
        return winner is None
