import random
import Dice
import Player


def main():
    print("Hello! Welcome to a game of Pig!")
    print("")
    print("           9")
    print("     ,--.-'-,--.")
    print("     \\  /-~-\\  /")
    print("    / )' a a `( \\")
    print("   ( (  ,---.  ) )")
    print("    \\ `(_o_o_)' /")
    print("     \\   `-'   /")
    print("      | |---| |  ")
    print("      [_]   [_]")
    print("")
   
    while True:
        print(">> PLAY <<")
        print(">> HIGHSCORE <<")
        print(">> EXIT <<")
        print("   m___")
        print("@=" + '""' + "~~" + '")' + ")")
        print("   " + "W  W") 
        
        choice = input("Enter Your Choice: ")

        if choice == "play" or choice == "Play":
            while True:
                # playersName = input("Enter your name: ")
                # creatingPlayer = Player.Player(playersName)
                # print(creatingPlayer)

                resultOfDice = 0

                while resultOfDice != 1:
                    playerThrowingDice = int(input("Enter 0 to throw the dice: "))
                    resultOfDice += resultOfDice
            
                if playerThrowingDice == 0:
                    resultOfDice = random.randint(1, 6)
                    thrownDice = Dice.Dice(resultOfDice)
                    sum = thrownDice.throwDice(resultOfDice)
                    print(sum)

                    tryAgain = input("Do you want to throw again? Enter yes or no: ")
                    if tryAgain.lower() == "yes":
                        print("Good luck!")

                    elif tryAgain.lower() == "no":
                        if resultOfDice > 0:
                            print(f"Congratulations! You got {resultOfDice} points from this round")
                        else: 
                            print("You got no points from this round, better luck next time!")
                        break
                    else: 
                        print("Not a valid option.")
                else:
                    print("Not a valid option")
        else:
            print("Not a valid option.")


if __name__ == "__main__":
    main()



