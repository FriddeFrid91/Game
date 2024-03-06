class DiceHand: 
    """A hand of dice for a player"""

    def __init__(self, dice, player, points):
        self.dice = dice
        self.player = player
        self.points = points
      
    def countRound(listOfPoints):
        totalPoints = 0
        for a in listOfPoints:
            totalPoints += a
        return totalPoints
    """Count current round"""

    def __str__(self):
        """Return a string representation of the hand"""
        return f"{self.player} has {self.dice} dice"
