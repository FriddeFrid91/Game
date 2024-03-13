from Dice import Dice
from Player import Player

"""The Game Class. Contains the game logic for the game of Pig."""


class Game:
    """The Game Class. Contains the game logic for the game of Pig."""

    def __init__(self):
        """Constructor for the Game class."""
        self.players = []
        self.player = Player(name="", score=0)
        self.dice = Dice(6)
        self.points = 0

    def __str__(self):
        """Return the result of the game."""
        return "Result: Players"
        
    def player_vs_computer(self, player1, intelligence):
        """Start the game. Player vs Computer."""
        self.players[currentPlayer] = 0
        self.players[intelligence] = 0
        self.scores = self.players

        currentPlayer = player1
        dice = Dice(6)

        while True:
            roll_the_dice = input(f"Players {currentPlayer.name} turn "
                                  + "- please enter 0 to roll the dice: ")
            if roll_the_dice == "0":
                result = dice.roll_the_dice()
                points_from_new_round = dice.show_the_dice(get.result())

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
                    currentPlayer = intelligence if currentPlayer == player1 else player2

    def player_vs_player(self, player1, player2):
        """Start the game. Player vs Player."""
        current_player = player1
        rolling_total = []
            
        while True:
            print(">> Player vs Player <<\n")
            print("")
            print(f"{player1.get_name()} has {player1.get_score()} points.")
            print(f"{player2.get_name()} has {player2.get_score()} points.\n")

            print("-----------------------------------------")
            print(f"{current_player.get_name()} is playing.")
            print("-----------------------------------------\n")

            roll_the_dice = input("Press enter to roll the dice. ")
            if roll_the_dice == "":
                roll = self.dice.roll_the_dice()  
                tot = self.dice.show_the_dice(roll)
                
                if roll != 1:
                    print(f"You rolled a {roll}.")
                    rolled = 0
                    rolling_total.append(roll)
                    for a in rolling_total:
                        rolled += a
                    print(f"You got {rolled} points from this round.")

                if roll == 1:
                    current_player.deduct_score(rolled)
                    rolling_total.clear()
                    if current_player == player1:
                        current_player = player2  
                                 
                        print(f"{player1.get_name()} has {player1.get_score()} points.")
                        print(f"{player2.get_name()} has {player2.get_score()} points.\n")
                    else:
                        rolling_total.clear()
                        current_player = player1                    
                        print(f"{player1.get_name()} has {player1.get_score()} points.")
                        print(f"{player2.get_name()} has {player2.get_score()} points.\n")

                elif tot > 1:
                    current_player.add_score(tot)
                    if current_player.get_score() >= 50:
                        print(f"{current_player.get_name()} has won the game!")
                        return current_player.get_name()            

                    hold = input("Do you want to hold? Yes or no: ")
                    if hold.lower() == "yes":
                        rolling_total.clear()
                        if current_player == player1:
                            current_player = player2
                          
                        else:
                            rolling_total.clear()
                            current_player = player1
                        
                    elif hold.lower() == "no":
                        continue
                    else:
                        print("Invalid input. Press write 'yes' or 'no'"
                              + " to roll the dice.")
                        continue
            else:
                print("Invalid input. Press enter to roll the dice.")
                continue
