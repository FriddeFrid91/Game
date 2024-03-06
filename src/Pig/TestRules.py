import unittest
from Rules import Rules

def main():
    """Run the test."""
    TestRules().setUp()
    unittest.main()


class TestRules(unittest.TestCase):
    def test_showRules(self):
        rules = Rules()
        self.assertEqual(rules.showRules(), "The game of Pig is a simple two-player dice game in which the first player to reach 100 or more points wins.")

    def test_showRules(self):
        rules = Rules()
        self.assertEqual(rules.showRules(), "1. The game is played with a single six-sided die.\n2. The game has two players, who take turns.\n3. On each turn, a player rolls the die as many times as they want, or until they roll a 1.\n4. Each number they roll, except for a 1, is added to their score this turn; but if they roll a 1, their score for this turn is zero, and their turn ends.\n5. At the end of each turn, the score for that turn is added to the player's total score.\n6. The first player to reach or exceed 100 wins.\n9. If a player rolls a 1, they lose all points for that turn and the other player starts their turn.")


if __name__ == "__main__":
    main()