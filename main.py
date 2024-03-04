def main():

    import Dice

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
    print("* 3. Quit              *")  
    print("************************\n")
    option = int(input("Please enter a option:"))

    while True:

        if option == 1:
            rolltheDice = int(input("Players turn - please enter 0 to roll the"
                                    + " dice."))
            if rolltheDice == 0:
                # Skapar en instans av Dice-klassen
                dice = Dice.Dice(6)
                resulOfDice = dice.showDiceRolls(1)
                print(f" You got a {resulOfDice}! ")
                input("Do you want to roll a again?")


if __name__ == "__main__":
    main()