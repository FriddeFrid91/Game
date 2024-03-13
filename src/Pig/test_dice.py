"""Test File for Unit Testing Dice.py."""

import unittest
from Dice import Dice


def main():
    """Run the test."""
    test_dice().setUp()
    unittest.main()


class test_dice(unittest.TestCase):
    """Test the Computer class."""

    def setUp(self):
        """Set the TestDice."""
        self.dice = Dice(6)

    def test_dice(self):
        """Test the Computer class."""
        self.assertIsInstance(self.dice, Dice)

    def test_roll_the_dice(self):
        """Test rollTheDice method."""
        result = self.dice.roll_the_dice()
        self.assertLessEqual(result, 6)
        self.assertGreaterEqual(result, 1)
  
    def test_show_the_dice(self):  
        """Test showTheDice method."""
        result = self.dice.roll_the_dice()
        self.assertLessEqual(result, 6)
        self.assertGreaterEqual(result, 1)
        self.assertEqual(result, self.dice.show_the_dice(result))

    def get_dice(self):
        """Test getDice method."""
        self.assertEqual(self.dice.getDice(), 6)
    
    def set_dice(self):
        """Test setDice method."""
        self.dice.setDice(6)
        self.assertEqual(self.dice.getDice(), 6)


if __name__ == "__main__":
    main()
