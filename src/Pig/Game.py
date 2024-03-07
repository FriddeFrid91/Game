"""The Game Class. Contains the game logic for the game of Pig."""
from Dice import Dice

'''The Game Class. Contains the game logic for the game of Pig.'''



class Game:
    """The Game Class. Contains the game logic for the game of Pig."""

    def __init__(self):
        """Create the dicitonary to store the players and their scores."""
        self.players = {}

    def __str__(self):
        """Return the result of the game."""
        return f"Result: {self.players.items()}"  

    def PlayerVsPlayer(self, player1, player2):
        """Start the game. Player vs Player."""
        self.players[player1] = 0
        self.players[player2] = 0
        self.scores = self.players

        print(">> Player vs Player <<\n")
        currentPlayer = player1
        dice = Dice(6)
 
        while True:
            roll_the_dice = input(f"Players {currentPlayer.name} turn "
                                  + "- please enter 0 to roll the dice: ")
            if roll_the_dice == "0":
                result = dice.rollTheDice()
                points_from_new_round = dice.showTheDice(result)

                if result != 1:
                    self.players[currentPlayer] += points_from_new_round
                    print(f"Total points: {self.scores[currentPlayer]}")
                    if self.players[currentPlayer] >= 6:
                        print(f"Congratulations! {currentPlayer.name} wins!")
                        returnedDict = {key.name: value for key, value in self.players.items()}
                        for key, value in self.players.items():
                            print(f"{key.name} got {value} points.")
                        return returnedDict
                    elif self.players[currentPlayer] < 6:
                        roll_again = input("Do you want to roll again? Enter yes or no: ").lower()
                    print("")
                    if roll_again == "no":
                        print(f"Your turn is over. You got {self.scores[currentPlayer]} points.")
                        currentPlayer.score = self.players[currentPlayer]
                        currentPlayer = player2 if currentPlayer == player1 else player1
                else:
                    self.players[currentPlayer] += 0
                    currentPlayer = player2 if currentPlayer == player1 else player1

    def PlayerVsComputer(self, player1, intelligence):
        """Start the game. Player vs Computer."""
        self.players[player1] = 0
        self.players[intelligence] = 0
        self.scores = self.players

        currentPlayer = player1
        dice = Dice(6)

        while True:
            roll_the_dice = input(f"Players {currentPlayer.name} turn "
                                  + "- please enter 0 to roll the dice: ")
            if roll_the_dice == "0":
                result = dice.rollTheDice()
                points_from_new_round = dice.showTheDice(result)

                if result != 1:
                    self.players[currentPlayer] += points_from_new_round
                    print(f"Total points: {self.scores[currentPlayer]}")
                    if self.players[currentPlayer] >= 6:
                        print(f"Congratulations! {currentPlayer.name} wins!")
                        returnedDict = {key.name: value for key, value in self.players.items()}
                        for key, value in self.players.items():
                            print(f"{key.name} got {value} points.")
                        return returnedDict
                    elif self.players[currentPlayer] < 6:
                        roll_again = input("Do you want to roll again? Enter yes or no: ").lower()
                    print("")
                    if roll_again == "no":
                        print(f"Your turn is over. You got {self.scores[currentPlayer]} points.")
                        currentPlayer.score = self.players[currentPlayer]
                        currentPlayer = intelligence if currentPlayer == player1 else player1
                else:
                    self.players[currentPlayer] += 0
                    currentPlayer = intelligence if currentPlayer == player1 else player1
         
