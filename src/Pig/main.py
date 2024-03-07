"""Main module for the Pig game."""


def main():
    """Main function for the Pig game.:"""

    from Intelligence import Intelligence
    from Player import Player
    from Game import Game
    from Rules import Rules
    from HighScore import HighScore
    import sys

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
                # Computer method
                intelligence.intelligence_move()
                # Player method2

            elif option == 2:
                print(">> Player vs Player <<\n")
                playersName1 = input("Please enter your name (Player 1): ")
                player1 = Player(playersName1)
                playersName2 = input("Please enter your name (Player 2): ")
                player2 = Player(playersName2)
                newGame = Game()
                info_returned = newGame.PlayerVsPlayer(player1, player2)
          
            elif option == 3:
                try:
                    print(">> Highscore <<\n")
                    highScore = HighScore()
                    highScore.saveScore(info_returned)
                    tot = highScore.loadScore()
                    print(f"Highscore: {tot}")
                    back_to_the_menu = int(input("Enter 0 to go back to the menu: "))
                    if back_to_the_menu == 0:
                        print("Back to the menu.")
                except UnboundLocalError:
                    print("-------------------------")
                    print("No high score to show.")
                    print("Please play a game first.")
                    print("-------------------------")

            elif option == 4:
                print(">> Rules <<\n")
                the_rules = Rules("Rules of Pig")
                print(the_rules.showRules())
                back_to_the_menu = int(input("Enter 0 to go back to the menu: "))
                if back_to_the_menu == 0:
                    print("Back to the menu.")

            elif option == 5:
                print("Goodbye!")
                sys.exit()

            else:
                print("---------------------------------")
                print("Invalid option. Please try again.")
                print("---------------------------------")

        except ValueError:
            print("------------------------------------------")
            print("Invalid input. Please enter a option 1-5.")
            print("------------------------------------------")


if __name__ == "__main__":
    main()
