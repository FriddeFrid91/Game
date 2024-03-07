"""The main function of the game. Contains the menu for the game."""


def main():
    """The main function of the game. Contains the menu for the game."""

    from Intelligence import Intelligence
    from Rules import Rules
    from Player import Player
    from Game import Game
    from HighScore import HighScore
    import sys
    # import cmd

    while True:
        print("Hello! Welcome to a game of Pig!")
        print("*************************")
        print("* 1. Player vs Computer *")
        print("* 2. Player vs Player   *")
        print("* 3. Highscore          *")
        print("* 4. Rules              *")
        print("* 5. Quit               *")
        print("*************************")

        try:
            option = int(input("Please enter an option: "))

            if option == 1:
                print(">> Player vs Computer <<\n")
                intelligence = Intelligence()
                game = Game()
                game.PlayerVsComputer(intelligence)

            elif option == 2:
                print(">> Player vs Player <<\n")
                playersName1 = input("Please enter your name (Player 1): ")
                player1 = Player(playersName1)
                playersName2 = input("Please enter your name (Player 2): ")
                player2 = Player(playersName2)
                game = Game()
                game.PlayerVsPlayer(player1, player2)

            elif option == 3:
                print(">> Highscore <<\n")
                highScore = HighScore()

            elif option == 4:
                print(">> Rules <<\n")
                rules = Rules()
                rules.showRules()
                backToMenu = input("Enter 0 to go back to the main menu: ")
                if backToMenu == "0":
                    print("Going back to the main menu.")

            elif option == 5:
                print("Goodbye!")
                sys.exit()

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
