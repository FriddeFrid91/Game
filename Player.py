class Player:
    def __init__(self, player, score):
        self.player = player
        self.name = player
        self.score = score

    def nameTaken(name):
        with open("players.txt", "r") as file:
            for line in file:
                if name in line:
                    return True
            return False

    def creatingPlayer(playersName, score):
        playersAndScores = {}
        if not Player.nameTaken(playersName):  
            with open("players.txt", "a") as file:
                file.write(f"{playersName}, {score}\n")
                return f"You entered: {playersName}"

    def showPlayers():
        with open("players.txt", "r") as file:
            for line in file:
                print(line.strip())  

    def playersScore(self):
        return self.score

