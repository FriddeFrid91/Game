import random
from Game import Game
from Player import Player
from Rules import Rules
from HighScore import HighScore
from Intelligence import Intelligence
import sys


<<<<<<< HEAD



def main():
=======
def main():
    """Main function for the Pig game."""
 
>>>>>>> 45450f51e002e8f2a7913ebc53d7929a5d150fe2
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
<<<<<<< HEAD
                    print(">> Player vs Computer <<\n")
                    intelligence = Intelligence()
                    game = Game()
                    # Computer method
                    intelligence.intelligence_move() 
                     # Player method2
                    player1 = input("Please enter your name: ")
                    player1 = Player(Game)
                    infoReturned = game.PlayerVsComputer(player1, intelligence)
=======
                print(">> Player vs Computer <<\n")
                # Computer method
                Intelligence.intelligence_move(11)
                # Player method2
                currentPlayer = input("Please enter your name: ")
                player1 = Player(Game)
                game = Game()
                infoReturned = game.player_vs_computer(player1, Intelligence)

                # Player method2
>>>>>>> 45450f51e002e8f2a7913ebc53d7929a5d150fe2

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
<<<<<<< HEAD
                        print(">> Highscore <<\n")
                        highScore = HighScore()
                        highScore.saveScore(infoReturned)
                        tot = highScore.loadScore()
                        print(f"Highscore: {tot}")
                        backToTheMenu = int(input("Enter 0 to go back to the menu: "))
                        if backToTheMenu == 0:
                            print("Back to the menu.")
=======
                    print(">> Highscore <<\n")
                    highscore = HighScore()
                    highscore.save_score(winner)
                    # show_score = highscore.load_score()
                    # print(show_score)
                    highscore.get_highScore()
                    show_score2 = highscore.get_highScore()
                    print(show_score2)
                    back_to_the_menu = int(input("Enter 0 to go back to the menu: "))
                    if back_to_the_menu == 0:
                        print("Back to the menu.")

>>>>>>> 45450f51e002e8f2a7913ebc53d7929a5d150fe2
                except UnboundLocalError:
                        print("-------------------------")
                        print("No high score to show.")
                        print("Please play a game first.")
                        print("-------------------------")

            elif option == 4:
                    print(">> Rules <<\n")
                    theRules = Rules("Rules of Pig")
                    print(theRules.show_rules())

            elif option == 5:
                    print("Goodbye!")
                    break
                    sys.exit()

            else:
                    print("---------------------------------")
                    print("Invalid option. Please try again.")
                    print("---------------------------------")
<<<<<<< HEAD

                
        except ValueError:
                print("------------------------------------------")
                print("Invalid input. Please enter a option 1-5.")
                print("------------------------------------------")
                
=======
        except ValueError:
            print("------------------------------------------")
            print("Invalid input. Please enter a option 1-5.")
            print("------------------------------------------")

>>>>>>> 45450f51e002e8f2a7913ebc53d7929a5d150fe2

if __name__ == "__main__":
    main()
    