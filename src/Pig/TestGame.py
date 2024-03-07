"""Test File for Unit Testing Game.py."""

import unittest
from Game import Game


def main():
    """Run the test."""
    TestGame().setUp()
    unittest.main()


class TestGame(unittest.TestCase):
    """Test the Game class."""

    def setUp(self):
        """Set the TestGame."""
        self.players = {}

    def test_playerVsPlayer(self):
        """Test rollTheDice method."""
        self.players = {}
        self.players["player1"] = 0
        self.players["player2"] = 0
        self.scores = self.players

        self.assertEqual(self.players["player1"], 0)
        self.assertEqual(self.players["player2"], 0)
        self.assertEqual(self.scores, self.players)


if __name__ == "__main__":
    main()
    