
"""The HighScore class. Contains the high score logic for the game of Pig."""
import pickle


class HighScore:
    """The HighScore class. Contains the high score logic for the game of Pig."""
 
    def __init__(self):
        """Create the high score."""
        self.score = 0

    def saveScore(self, dictOfScores, highScorez):
        """Save the high score to a file."""
        with open(highScorez, "wb") as file:
            pickle.dump(dictOfScores, file)

    def loadScore(self, HighScorez):
        """Load the high score from a file."""
        try:
            with open(HighScorez, "rb") as file:
                pickle.load(file)
                for line in file:
                    print(line)
            return self.score
        except FileNotFoundError:
            print("No high score found. Starting a new game.")
            self.score = 0

    def showHighScore(self):
        print(f"The current high score is: {self.score}")

    #def updateHighScore(self, score):
        #if score > self.score:
            #self.score = score
            #print("Congratulations! You have a new high score!")
            #self.saveScore()
       # else:
          #  print("You did not beat the high score this time.")

    def addScore(self, score):
        self.score += score

    def getScore(self):
        return self.score

    def resetScore(self):
        self.score = 0
