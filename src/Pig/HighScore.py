
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
        old_score = self.dict_of_highscores
        new_info = {winner: 1}
        if winner is None:
            print("Highscore not updated.")
            print("Why? Because there is no winner.")
            for a in old_score:
                print(f"{a} has {old_score[a]} wins.")
            return
     
        print(f"{new_info} OK")
        try:
            with open(self.filename, "rb") as file:
                self.dict_of_highscores = pickle.load(file)
                print(f"{self.dict_of_highscores} OK")

        except FileNotFoundError:
            self.dict_of_highscores = {winner: 1}
                                 
            if winner in self.dict_of_highscores:
                self.dict_of_highscores[winner] += 1
            else:
                self.dict_of_highscores[winner] = 1
            return winner == 0
        
        else:
            with open(self.filename, "wb") as file:
                pickle.dump(self.dict_of_highscores, file)

        for a in self.dict_of_highscores:
            print(f"{a} has {self.dict_of_highscores[a]} wins.")

    def get_highScore(self):
        """Get the high score."""
        return self.dict_of_highscores