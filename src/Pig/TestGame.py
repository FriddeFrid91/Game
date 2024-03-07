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
        result = self.dice.rollTheDice(result=6)
        self.assertLessEqual(result, 6)
        self.assertGreaterEqual(result, 1)


if __name__ == "__main__":
    main()
    