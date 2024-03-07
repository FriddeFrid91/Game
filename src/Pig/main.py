def main():

    import cmd  
    from Intelligence import Intelligence
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
                newGame.PlayerVsPlayer(player1, player2, listOfPoints)
                
            elif option == 3:
                print(">> Highscore <<\n")
                highScore = HighScore()
                highScore.saveScore(infoReturned)
                tot = highScore.loadScore()
                highScore.showHighScore()
                # highScore.updateHighScore(infoReturned)
                print(tot)

                print(infoReturned)
                print(">> Highscore <<\n")
                # Implement highscore display
                if infoReturned is not None:
                    print(">> Highscore <<\n")
                    highScore = HighScore()
                    highScore.saveScore()
                    highScore.loadScore()
                    highScore.showHighScore()
                    # highScore.updateHighScore(infoReturned)

                    print(infoReturned)

            elif option == 4:
                print(">> Rules <<\n")
                theRules = Rules("Rules of Pig")
                theRules.showRules()
                
            elif option == 5:
                print("Goodbye!")
                break  # Exit the loop and end the program

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("------------------------------------------")
            print("Invalid input. Please enter a option 1-5.")
            print("------------------------------------------")

if __name__ == "__main__":
    main()
