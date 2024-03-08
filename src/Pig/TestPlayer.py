"""Test File for Unit Testing Player.py."""

import unittest
from Player import Player


def main():
    """Run the test."""
    TestPlayer().setUp()
    unittest.main()


class TestPlayer(unittest.TestCase):
    """Test the Computer class."""

    def setUp(self):
        """Set the TestPlayer."""
        self.player = Player(name="", score=0)
        self.player.name = "Test"

    def test_player_vs_player(self):
        """Test the Computer class."""
        self.assertIsInstance(self.player, Player)


if __name__ == "__main__":
    main()
