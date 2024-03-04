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
    print("************************")
         
    # Skapar en instans av Dice-klassen
    dice = Dice.Dice(6)
   
    dice.showDiceRolls(1)


if __name__ == "__main__":
    main()