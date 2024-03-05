class DiceHand: 
    """A hand of dice for a player"""

    def __init__(self, dice, player, points):
        self.dice = dice
        self.player = player
        self.points = points
       
    def countCurrentRound(self, points):
        totalPoints = 0
        totalPoints += points
        return totalPoints
        """Count current round"""

    def __str__(self):
        """Return a string representation of the hand"""
        return f"{self.player} has {self.dice} dice"
   
