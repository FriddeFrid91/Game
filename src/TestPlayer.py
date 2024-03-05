import unittest
from Player import Player


class TestPlayerClass(unittest.TestCase):
    """Test the Player class"""
    def test_creatPlayer(self):
        """Test the createPlayer method"""
        creatingPlayer = Player("Test")
        self.assertEqual(creatingPlayer.name, "Test")
