class Player:
    def __init__(self, player, score):
        self.player = player
        self.name = player
        self.score = score
  
    def creatingPlayer(playersName, score):
        # filename = "players.txt"
        with open("players.txt", "a") as file:
            file.write(f"{playersName}\nScore: {score}\n")

    def showPlayers():
        with open("players.txt", "r") as file:
            for a in file:
                return (a)

    def playersScore():
        pass
