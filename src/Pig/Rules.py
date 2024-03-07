"""This module is used to display the rules of the game."""


class Rules:
    """This class is used to display the rules of the game."""
 
    def __init__(self, rules):
        """Create the rules of the game."""
        self.rules = rules

    def showRules(self):
        """Show the rules of the game."""
        rules_text = """
        >> Pig is a simple dice game where the goal is to reach 100 points first. <<
        Players take turns rolling a single six-sided die: 
        If the player rolls a 1, they score no points and lose their turn.
        If the player rolls any other number, it is added to their turn total and their turn continues.
        Players can choose to "hold", which adds their turn total to their score and ends their turn.
        The first player to reach or exceed 100 points wins the game.
        """
        return rules_text

    def __str__(self):
        """Return the rules of the game."""
        return self.rules
