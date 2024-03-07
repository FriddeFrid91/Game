class Rules:
    def __init__(self):
        self.rules = "Rules"

    def showRules(self):
        print("1. The game is played with a single six-sided die.")
        print("2. The game has two players, who take turns.")
        print("3. On each turn, a player rolls the die as many times as they want, or until they roll a 1.")
        print("4. Each number they roll, except for a 1, is added to their score this turn; \nbut if they roll a 1, their score for this turn is zero, and their turn ends.")
        print("5. At the end of each turn, the score for that turn is added to the player's total score.")
        print("6. The first player to reach or exceed 100 wins.")
        print("9. If a player rolls a 1, they lose all points for that turn and the other player starts their turn.")