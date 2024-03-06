from Dice import Dice
from Player import Player
from DiceHand import DiceHand


class Game(Dice, Player):
    def __init__(self):
        self.listOfPoints = []
        self.players = []

    def PlayerVsPlayer(self, player1, player2, listOfPoints):
        self.players.append(player1)
        self.players.append(player2)    

        print(">> Player vs Player <<\n")
        while True:
            rolltheDice = input("Player's turn - please enter 0 to roll the dice: ")
            if rolltheDice == "0":
                # Assuming Dice class is defined elsewhere in your code
                dice = Dice(6)  
                result = dice.rollTheDice(dice)
                diceOne = dice.showTheDice(result, listOfPoints)
                listOfPoints.append(result)
                pointsFromNewRound = DiceHand.countRound(listOfPoints)
                if diceOne == 1:
                    listOfPoints.clear()
                    appendPoints = player1.addPoints(0)
                    break
                else:
                    appendPoints = player1.addPoints(pointsFromNewRound)
                    print(pointsFromNewRound)
                    rollAgain = input("Do you want to roll again? Please enter yes or no: ")
                    print("")
                    if rollAgain.lower() == "yes":
                        print("Good luck!")
                        continue
                    elif rollAgain.lower() == "no":
                        print("Your turn is over.")
                        break
                    print("")
