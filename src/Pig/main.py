def main():

    import cmd
    from Dice import Dice
    from Rules import Rules
    from DiceHand import DiceHand
    from Player import Player
    listOfPoints = []
    dictOfPlayers = {}
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
        playersName1 = input("Please enter your name (Player 1): ")
        print(f"You entered: {playersName1}")
        player1 = Player("Player 1")
        # player1.createPlayer(playersName1)
        player1.name = playersName1
        player1.score = 0
        dictOfPlayers[player1] = 0
        print(dictOfPlayers.values())

        playersName2 = input("Please enter your name (Player 2): ")
        print(f"You entered: {playersName2}")
        player2 = Player("Player 2")
        player2.score = 0
        player2.createPlayer(playersName2)
        dictOfPlayers[playersName2] = 0
        dictOfPlayers[player2.name] = player2.score
        print(dictOfPlayers.values())

        option = int(input("Please enter a option: \n"))

        while True:
            print(">> Player vs Computer <<\n")
            if option == 1:
                rolltheDice = int(input("Players turn - please enter 0 to roll"
                                        + " the dice. "))
                if rolltheDice == 0:
                    # Skapar en instans av Dice-klassen
                    dice = Dice(6)  
                    result = dice.rollTheDice(dice)
                    if result == 1:
                        print("Sorry, you got a 1. Your turn is over.")
                        break
                    print(f"You got a {result}!")
                    listOfPoints.append(result)
                    pointsFromNewRound = DiceHand.countRound(listOfPoints)
                    print(pointsFromNewRound)

                    print("")
                    
                    rollAgain = input("Do you want to roll a again? Please "
                                      + "enter yes or no: ")
                    print("")
                    if rollAgain.lower() == "yes":
                        print("Good luck!")
                        continue
                    elif rollAgain.lower() == "no":
                        print("Your turn is over.")
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
                rules = Rules("Rules of Pig")
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
