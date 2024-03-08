"""This module is used to display the rules of the game."""


class Rules:
    """This class is used to display the rules of the game."""

    def __init__(self, rules):
        """Create the rules of the game."""
        self.rules = rules

    def show_rules(self):
        """Show the rules of the game."""
        rules_text = "rules.txt"
        with open(rules_text, "r") as file:
            rules_text = file.read()
        return rules_text

    def __str__(self):
        """Return the rules of the game."""
        return self.rules
