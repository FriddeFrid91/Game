"""Test File for Unit Testing HighScore.py."""

import unittest
from HighScore import HighScore

"""The HighScore class. Contains the high score logic for the game of Pig."""


def main():
    """Run the test."""
    test_highscore().setUp()
    unittest.main()


class test_highscore(unittest.TestCase):
    """Test the Game class."""

    def setUp(self):
        """Set the TestGame."""
        self.players = {}

    def test_load_score(self):
        """Test load_score method."""
        self.highScore = HighScore()
        self.assertIsInstance(self.highScore, HighScore)
        self.assertEqual(self.highScore.load_score(), None)

    def test_save_score(self):
        """Test save_score method."""
        self.highScore = HighScore()
        self.assertIsInstance(self.highScore, HighScore)


if __name__ == "__main__":
    main()