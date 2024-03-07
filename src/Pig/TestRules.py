import unittest
from Rules import Rules
"""This module is used to test the Rules class."""


def main():
    """Run the test."""
    TestRules().setUp()
    unittest.main()


class TestRules(unittest.TestCase):
    """Test the Rules class."""

    def setUp(self):
        """Set the TestRules."""
        self.rules = Rules("Pig game rules.")

    def test_rules(self):
        """Test the Rules class."""
        self.assertIsInstance(self.rules, Rules)

    def test_showRules(self):
        """Test showRules method."""
        self.rules.showRules()
        self.assertIsNotNone(self.rules.showRules())


if __name__ == "__main__":
    main()