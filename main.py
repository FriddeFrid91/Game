import random
import Dice


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
        
        choice = input("Enter Your Choice: ")

        if choice == "play" or choice == "Play":
            while True:
                playerThrowingDice = int(input("Enter 0 to throw the dice: "))
                print("   m___")
                print("@=" + '""' + "~~" + '")' + ")")
                print("   " + "W  W") 

                if playerThrowingDice == 0:
                    resultOfDice = random.randint(1, 6)
                    thrownDice = Dice.Dice(resultOfDice)
                    print(thrownDice.throwDice(resultOfDice))

                    diceHand = resultOfDice + resultOfDice

                    tryAgain = input("Do you want to throw again? Enter yes or no: ")
                    if tryAgain.lower() == "yes":
                        print("Good luck!")
                    elif tryAgain.lower() == "no":
                        if diceHand > 0:
                            print(f"Congratulations! You got {diceHand} points from this round")
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



