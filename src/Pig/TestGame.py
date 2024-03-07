"""Test File for Unit Testing Game.py."""

import unittest
from Game import Game


def main():
    """Run the test."""
    TestDice().setUp()
    unittest.main()


class TestDice(unittest.TestCase):
    """Test the Game class."""

    def setUp(self):
        """Set the TestDice."""
        self.players = {}

    def test_dice(self):
        """Test the Game Class."""
        self.assertIsInstance(self.dice, Dice)

    def test_rollTheDice(self):
        """Test rollTheDice method."""
        result = self.dice.rollTheDice(result=6)
        self.assertLessEqual(result, 6)  
        self.assertGreaterEqual(result, 1)


if __name__ == "__main__":
    main()