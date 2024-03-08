
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
        new_info = {winner: 1}
        print(f"{new_info} OK")
        try:
            with open(self.filename, "rb") as file:
                self.dict_of_highscores = pickle.load(file)
                print(f"{self.dict_of_highscores} OK")
                if winner in self.dict_of_highscores:
                    self.dict_of_highscores[winner] += 1
                else:
                    self.dict_of_highscores.update(new_info)
                    
                
        except FileNotFoundError:
            with open(self.filename, "wb") as file:
                pickle.dump(new_info, file)
                
                
                with open(self.filename, "wb") as file:
                    pickle.dump(self.dict_of_highscores, file)

        sorted_dict = dict(sorted(self.dict_of_highscores.items(), key=lambda x: x[1]))

        print(">> Highscore <<")
        self.dict_of_highscores = sorted_dict
        for a in sorted_dict:
            print(f"{a} has {sorted_dict[a]} wins.")

        for a in self.dict_of_highscores:
            print(f"{a} has {self.dict_of_highscores[a]} wins.")

    def get_highScore(self):
        """Get the high score."""
        return self.dict_of_highscores