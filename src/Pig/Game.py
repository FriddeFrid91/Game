"""The Game Class. Contains the game logic for the game of Pig."""
from Dice import Dice


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
