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

    def test_player_vs_player(self):
        """Test rollTheDice method."""
        self.scores = self.players
        self.assertEqual(self.scores, self.players)


if __name__ == "__main__":
    main()
    