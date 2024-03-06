def main():
    import cmd
    from Player import Player
    from Game import Game
    from Rules import Rules

    listOfPoints = []

    while True:
        print("Hello! Welcome to a game of Pig!")
        print("*************************")
        print("* 1. Player vs Computer *")
        print("* 2. Player vs Player   *")
        print("* 3. Highscore          *")
        print("* 4. Rules              *")
        print("* 5. Quit               *")
        print("*************************")

        option = int(input("Please enter an option: "))

        if option == 1:
            print(">> Player vs Computer <<\n")
            # Implement one-player mode here
            
        elif option == 2:
            print(">> Player vs Player <<\n")
            playersName1 = input("Please enter your name (Player 1): ")
            player1 = Player(playersName1)
            playersName2 = input("Please enter your name (Player 2): ")
            player2 = Player(playersName2)
            newGame = Game()
            newGame.PlayerVsPlayer(player1, player2, listOfPoints)
            break

        elif option == 3:
            print(">> Highscore <<\n")

            # Implement highscore display
            
        elif option == 4:
            print(">> Rules <<\n")
            theRules = Rules("Rules of Pig")
            theRules.showRules()
            break
            
        elif option == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
