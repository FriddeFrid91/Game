"""Test File for Unit Testing Player.py."""

import unittest
from Player import Player


def main():
    """Run the test."""
    test_player().setUp()
    unittest.main()


class test_player(unittest.TestCase):
    """Test the Computer class."""

    def setUp(self):
        """Set the TestPlayer."""
        self.player = Player(name="", score=0)
        self.player.name = "Test"

    def test_player(self):
        """Test the Computer class."""
        self.assertIsInstance(self.player, Player)

    def test_player_vs_player(self):
        """Test the Computer class."""
        self.assertIsInstance(self.player, Player)
        self.assertIsNotNone(self.player)
        self.assertEqual(self.player.get_name(), "Test")
        self.addCleanup(self.player.get_name)
        self.assertCountEqual(self.player.get_name(), "Test")

    def test_player_vs_player(self):
        """Test the Computer class."""
        self.assertIsInstance(self.player, Player)
  
    def test_player_name(self):
        """Test the name of the player."""
        self.assertEqual(self.player.get_name(), "Test")  

    def deduct_score(self):
        """Test the deduct_score method."""
        self.player.deduct_score(1)
        self.assertEqual(self.player.get_score(), 0)


if __name__ == "__main__":
    main()
