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
        print("1. PLAYER VS COMPUTER <<")
        print("2. TWO PLAYER <<")
        print("3. HIGHSCORE <<")
        print("4. EXIT <<\n")

        choice = int(input("Enter Your Choice: "))

        if choice == 2:
            playersName1 = input("Player 1: Enter your name: ")

            Player.Player(playersName1, 0)
            sum = Player.Player.nameTaken(playersName1)
            print(sum)
            Player.Player.creatingPlayer(playersName1, 0)

            playersName2 = input("Player 2: Enter your name: ")

            Player.Player(playersName2, 0)
            sum1 = Player.Player.nameTaken(playersName2)
            print(sum1)
            Player.Player.creatingPlayer(playersName2, 0)

            while True:
                enterKey = input("Enter 0 to roll the dice: ")
                if enterKey == "0":
                    rolledDice = random.randint(1, 6)
                    print(f"You got a {rolledDice}!")
                    print("---------------")
                    if rolledDice > 1:
                        listOfPoints.append(rolledDice)
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
