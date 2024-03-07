"""The Game Class. Contains the game logic for the game of Pig."""
from Dice import Dice


class Game:
    """   The Game Class. Contains the game logic for the game of Pig."""
    def __init__(self):
        """Create the dicitonary to store the players and their scores."""
        self.players = {}

    def PlayerVsPlayer(self, player1, player2):
        """Start the game. Player vs Player."""
        self.players[player1] = 0
        self.players[player2] = 0
        self.scores = self.players

        print(">> Player vs Player <<\n")
        currentPlayer = player1
        dice = Dice(6)

        while True:
            roll_the_dice = input(f"Player {currentPlayer.name} turn - please enter 0 to roll the dice: ")
            if roll_the_dice == "0":
                result = dice.rollTheDice()
                points_from_new_round = dice.showTheDice(result)

                if result != 1:
                    self.players[currentPlayer] += points_from_new_round
                    print(f"Total points: {self.scores[currentPlayer]}")
                    roll_again = input("Do you want to roll again? Please enter yes or no: ").lower()
                    print("")
                    if roll_again == "no":
                        print(f"Your turn is over. You got {self.scores[currentPlayer]} points.")
                        totalPointsFromRound = currentPlayer.score = self.players[currentPlayer]
                        print(f"What {totalPointsFromRound}")
                        currentPlayer = player2 if currentPlayer == player1 else player1
                else:
                    self.players[currentPlayer] += 0
                    currentPlayer = player2 if currentPlayer == player1 else player1

                if self.players[currentPlayer] >= 20:
                    print(f"Congratulations! {currentPlayer.name} wins!")
                    break
