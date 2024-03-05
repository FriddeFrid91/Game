import unittest
from Dice import Dice


class TestDiceClass(unittest.TestCase):
    """Test the Dice class"""
    def test_rollTheDice(self):
        """Test the rollTheDice method"""
        dice = Dice(6)
        result = dice.rollTheDice()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)


if __name__ == "__main__":
    unittest.main()