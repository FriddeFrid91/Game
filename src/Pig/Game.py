from Dice import Dice
from Player import Player
from DiceHand import DiceHand

class Game:
    def __init__(self):
        self.listOfPoints = []
        self.players = []

    def PlayerVsPlayer(self, player1, player2, listOfPoints):
        self.players.append(player1)
        self.players.append(player2)    

        print(">> Player vs Player <<\n")
        while True:
            rolltheDice = input(f"Player 1:s {player1} turn - please enter 0 to roll the dice: ")
            if rolltheDice == "0":
                dice = Dice(6) 
                result = dice.rollTheDice(dice)
                diceOne = dice.showTheDice(result, listOfPoints)
                listOfPoints.append(result)
                pointsFromNewRound = DiceHand.countRound(listOfPoints)
                if diceOne == 1:
                    listOfPoints.clear()
                    player1.addPoints(0)
                    print("Your turn is over.")
                    break
                else:
                    player1.addPoints(pointsFromNewRound)
                    print(pointsFromNewRound)
                    rollAgain = input("Do you want to roll again? Please enter yes or no: ")
                    print("")
                    if rollAgain.lower() == "no":
                        print("Your turn is over.")
                        break
