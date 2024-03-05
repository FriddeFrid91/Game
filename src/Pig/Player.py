"""Player class."""

import pickle

"""Player class."""


class Player:
    def __init__(self, name, level):
        """Player class."""
        self.name = name
        self.level = level

    def createPlayer(playersName):
        dictOfPlayers = {}
        print(f"You entered {playersName}")
        dictOfPlayers[playersName] = 0

        with open("players.txt", "wb") as playersFile:
            pickle.dump(dictOfPlayers, playersFile)
        return playersName 
   
    def showPlayer():
        """Player class."""
        with open("players.txt", "rb") as playersFile:
            player = pickle.load(playersFile)
            for line in player:
                print(line)
      
    def __str__(self):
        return f"{self.name} is a {self.level} player"
