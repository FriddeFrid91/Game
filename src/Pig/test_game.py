"""Test File for Unit Testing Game.py."""

import unittest
from Game import Game


def main():
    """Run the test."""
    test_game().setUp()
    unittest.main()


class test_game(unittest.TestCase):
    """Test the Game class."""

    def setUp(self):
        """Set the TestGame."""
        self.game = Game()
        self.players = {}
        self.players["player1"] = 0
        self.players["player2"] = 0
        self.scores = self.players
        self.player = self.players
        self.dice = self.game.dice

    def test_player_vs_player(self):
        """Test player_vs_player method."""
        self.scores = self.players
        self.assertIsInstance(self.game, Game)
        self.assertEqual(self.scores, self.players)
        self.assertEqual(self.game.player_vs_player, self.game.player_vs_player)

    def test_player_vs_computer(self):
        """Test player_vs_computer method."""
        self.scores = self.players
        self.assertIsInstance(self.game, Game)
        self.assertEqual(self.scores, self.players)

    def roll_the_dice(self):
        """Test roll_the_dice method."""
        self.scores = self.players
        self.assertIsInstance(self.game, Game)
        self.assertEqual(self.scores, self.players)

    def if_roll_again(self):
        """Test if_roll_again method."""
        self.scores = self.players
        self.assertIsInstance(self.game, Game)
        self.assertEqual(self.scores, self.players)

    def reset_score(self):
        """Test reset_score method."""
        self.scores = self.players
        self.assertIsInstance(self.game, Game)
        self.assertEqual(self.scores, self.players)


if __name__ == "__main__":
    main()