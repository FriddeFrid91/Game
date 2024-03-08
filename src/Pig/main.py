import random
from Game import Game
from Player import Player
from Rules import Rules
from HighScore import HighScore
from Intelligence import Intelligence
import sys


def main():
    """Main function for the Pig game."""
 
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
                    game = Game()
                    # Computer method
                    intelligence.intelligence_move() 
                     # Player method2
                    playerName = input("Please enter your name: ")
                    player = Player(name=playerName, score=0)
                    player.score = 0
                    player.player_move()
                    



            elif option == 2:
                    print(">> Player vs Player <<\n")
                    playersName1 = input("Please enter your name (Player 1): ")
                    player1 = Player(playersName1)
                    playersName2 = input("Please enter your name (Player 2): ")
                    player2 = Player(playersName2)
                    newGame = Game()
                    newGame.player_vs_player(player1, player2)      

            elif option == 3:
                try:
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
        except ValueError:
            print("------------------------------------------")
            print("Invalid input. Please enter a option 1-5.")
            print("------------------------------------------")


if __name__ == "__main__":
    main()
    