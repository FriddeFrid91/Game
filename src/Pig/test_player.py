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

    def test_player_move(self):
        """Test the player_move method."""
        self.player.player_move()
        self.assertIsNotNone(self.player.player_move())

    def get_name(self):
        """Test the get_name method."""
        self.assertEqual(self.player.get_name(), "Test")

    def get_score(self):
        """Test the get_score method."""
        self.assertEqual(self.player.get_score(), 0)

    def set_score(self):
        """Test the set_score method."""
        self.player.set_score(0)
        self.assertEqual(self.player.get_score(), 0)

    def change_name(self):
        """Test the change_name method."""
        self.player.change_name("Test")
        self.assertEqual(self.player.get_name(), "Test")
  
    def test_player_name(self):
        """Test the name of the player."""
        self.assertEqual(self.player.get_name(), "Test")

    def add_score(self):
        """Test the add_score method."""
        self.player.add_score(1)
        self.assertEqual(self.player.get_score(), 1)

    def deduct_score(self):
        """Test the deduct_score method."""
        self.player.deduct_score(1)
        self.assertEqual(self.player.get_score(), 0)


if __name__ == "__main__":
    main()
