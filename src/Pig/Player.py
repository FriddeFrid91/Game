class Player:
    """Class for creating a player."""
    def __init__(self):
        self.name = ""
        self.score = 0

    def __str__(self):
        return f"{self.name} has {self.score} points."
   
    def getName(self):
        """Get the name of the player."""
        return self.name
     
    def setName(self, name):
        """Set the name of the player."""
        self.name = name

    def getScore(self):
        """Get the score of the player."""
        return self.score
  
    def setScore(self, score):
        """Set the score of the player."""
        self.score = score

    def createPlayer(self):
        """Create a player."""
        while True:
            name = input("Enter your name: ")
            if name == "":
                print("You must enter a name.")
            else:
                change_name = input("Are you sure you want to use this name? "
                                    + "Yes or no: ")
                if change_name.lower() == "yes":
                    print(f"Welcome {name}!")
                    self.setName(name)
                    print(f"Player {self.getName()} has been created.")
                    return self.getName()
                elif change_name.lower() == "no":
                    continue
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")