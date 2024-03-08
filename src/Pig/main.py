import random
from Game import Game
from Player import Player
from Rules import Rules
from HighScore import HighScore
from Intelligence import Intelligence
import sys





def main():
    while True:
        """Main function for the Pig game."""
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
                    player1 = Player(input("Please enter your name: "))
                    game = Game()
                    # Computer method
                    intelligence.intelligence_move()
                     # Player method2
                    infoReturned = game.PlayerVsComputer(player1, intelligence)

            elif option == 2:
                    print(">> Player vs Player <<\n")
                    playersName1 = input("Please enter your name (Player 1): ")
                    player1 = Player(playersName1)
                    playersName2 = input("Please enter your name (Player 2): ")
                    player2 = Player(playersName2)
                    newGame = Game()
                    infoReturned = newGame.PlayerVsPlayer(player1, player2)
            
            elif option == 3:
                try:
                        print(">> Highscore <<\n")
                        highScore = HighScore()
                        highScore.saveScore(infoReturned)
                        tot = highScore.loadScore()
                        print(f"Highscore: {tot}")
                        backToTheMenu = int(input("Enter 0 to go back to the menu: "))
                        if backToTheMenu == 0:
                            print("Back to the menu.")
                except UnboundLocalError:
                        print("-------------------------")
                        print("No high score to show.")
                        print("Please play a game first.")
                        print("-------------------------")

            elif option == 4:
                    print(">> Rules <<\n")
                    theRules = Rules("Rules of Pig")
                    print(theRules.showRules())

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
    