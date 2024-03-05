import pickle


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def createPlayer(playersName):
        dictOfPlayers = {}
        print(f"You entered {playersName}")
        dictOfPlayers.update({playersName: 0})
        return playersName