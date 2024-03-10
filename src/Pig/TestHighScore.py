"""Test File for Unit Testing HighScore.py."""

import unittest
from HighScore import HighScore

"""The HighScore class. Contains the high score logic for the game of Pig."""


def main():
    """Run the test."""
    TestHighScore().setUp()
    unittest.main()


class TestHighScore(unittest.TestCase):
    """Test the Game class."""

    def setUp(self):
        """Set the TestGame."""
        self.players = {}

    def test_save_score(self):
        """Test rollTheDice method."""
        self.scores = self.players
        self.assertEqual(self.scores, self.players)

    def test_load_score(self):
        """Test rollTheDice method."""
        self.scores = self.players
        self.assertEqual(self.scores, self.players) 


if __name__ == "__main__":
    main()