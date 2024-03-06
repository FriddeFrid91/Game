"""Test File for Unit Testing Dice.py."""

import unittest
from Dice import Dice


def main():
    """Run the test."""
    TestDice().setUp()
    unittest.main()


class TestDice(unittest.TestCase):
    """Test the Computer class."""

    def setUp(self):
        """Set the TestDice."""
        self.dice = Dice(6)

    def test_dice(self):
        """Test the Computer class."""
        self.assertIsInstance(self.dice, Dice)

    def test_rollTheDice(self):
        """Test rollTheDice method."""
        self.assertLessEqual(self.dice.rollTheDice(), 6)  
        self.assertGreaterEqual(self.dice.rollTheDice(), 1)


if __name__ == "__main__":
    main()
