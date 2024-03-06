def main():

    import Dice
    from Rules import Rules
    from DiceHand import DiceHand
    from Player import Player
    while True:
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
        print("************************")
        print("* 1. One-Player        *")
        print("* 2. Two-Player        *")
        print("* 3. Highscore         *")
        print("* 4. Rules             *")
        print("* 5. Quit              *")
        print("************************")
        print("")
        playersName = input("Please enter your name: ")
        print(f"You entered: {playersName}")
        Player.createPlayer(playersName)

        option = int(input("Please enter a option: \n"))

        while True:
            print(">> Player vs Computer <<\n")
            if option == 1:
                rolltheDice = int(input("Players turn - please enter 0 to roll"
                                        + " the dice. "))
                if rolltheDice == 0:
                    # Skapar en instans av Dice-klassen
                    dice = Dice.Dice(6)
                    result = dice.showDiceRolls(1, dice.rollTheDice)
                    print(f"You got a {result}!")
                    DiceHand.countCurrentRound(result)
                    print("")
                    rollAgain = input("Do you want to roll a again? Please "
                                      + "enter yes or no: ")
                    print("")
                    if rollAgain.lower() == "yes":
                        print("Good luck!")
                        continue
                    elif rollAgain.lower() == "no":
                        break

            elif option == 2:
                print(">> Player vs player <<\n")

            elif option == 3:
                print(">> Highscore <<\n")
                Player.showPlayer()
                print("")
                highsScoreOption = int(input("Back to the main menu "
                                             + "- please enter 0: \n"))
                if highsScoreOption == 0:
                    break
                else:
                    print("Not a valid option.")
            elif option == 4:
                print(">> PIG GAME RULES <<\n")
                rules = Rules()
                rules.showRules()
                print("")
                rulesOption = int(input("Back to the main menu - "
                                        + "please enter 0: \n"))
                if rulesOption == 0:
                    break
                else:
                    print("Not a valid option.")
            elif option == 5:
                print("Goodbye!")
                break


if __name__ == "__main__":
    main()
