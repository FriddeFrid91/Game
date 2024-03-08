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

    def __str__(self):
        """Return the result of the game."""
        return "Result: Players"

    def player_vs_player(self, player1, player2):
        """Start the game. Player vs Player."""
        current_player = player1
        while True:
            print(">> Player vs Player <<\n")
            print(">> A new round of Pig is starting! <<")
            print(f"{player1.get_name()} has {player1.get_score()} points.")
            print(f"{player2.get_name()} has {player2.get_score()} points.")

            print(f"{current_player.get_name()} is playing.")
            roll_the_dice = input("Press enter to roll the dice. ")
            if roll_the_dice == "":
                roll = self.dice.roll_the_dice()
                tot = self.dice.show_the_dice(roll)
                if tot == 0:
                    current_player.reset_score()
                    if current_player == player1:
                        current_player = player2             
                    else:
                        current_player = player1
                elif tot > 1:
                    current_player.add_score(tot)
                    if current_player.get_score() >= 6:
                        print(f"{current_player.get_name()} has won the game!")
                        return current_player.get_name() 
                    print(f"{current_player.get_name()} has {current_player.get_score()} points.")
                    hold = input("Do you want to hold? Yes or no: ")
                    if hold.lower() == "yes":
                        if current_player == player1:
                            current_player = player2
                        else:
                            current_player = player1
                    elif hold.lower() == "no":
                        continue
                    else:
                        print("Invalid input. Press enter to roll the dice.")
            else:
                print("Invalid input. Press enter to roll the dice.")
