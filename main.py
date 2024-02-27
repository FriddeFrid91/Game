import random
import DiceHand
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
    listOfPoints = []
  
    while True:
        print(">> PLAY <<")
        print(">> HIGHSCORE <<")
        print(">> EXIT <<\n")

        choice = input("Enter Your Choice: ").lower()

        if choice == "play":
            playersName = input("Enter your name: ")

            Player.Player(playersName, 0)
            Player.Player.nameTaken(playersName)
            Player.Player.creatingPlayer(playersName, 0)

            while True:
                enterKey = input("Enter 0 to roll the dice: ")
                if enterKey == "0":
                    thrownDice = random.randint(1, 6)
                    print(f"You got a {thrownDice}!")
                    print("---------------")
                    if thrownDice > 1:
                        listOfPoints.append(thrownDice)
                        tot = DiceHand.DiceHand.countingTheRound(listOfPoints)
                        print(tot)
                        continueOrNot = input("Do you want to roll the dice again? Enter yes or no.\n")
                        if continueOrNot.lower() == "no":
                            print("End of your turn.")
                            break
                        if continueOrNot.lower() == "yes":
                            print("Good luck!")
                    else:
                        print("You got 0 points.")
                        print("End of your turn.")
                        break
        elif choice == "exit":
            print("Goodbye, thanks for playing!")
            break 


if __name__ == "__main__":
    main()





