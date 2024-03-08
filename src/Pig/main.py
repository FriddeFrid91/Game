"""Main module for the Pig game."""
 
from Intelligence import Intelligence
from Player import Player
from Game import Game
from Rules import Rules
from HighScore import HighScore
import sys


def main():
    """Main function for the Pig game."""
 
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
                # Computer method
                Intelligence.intelligence_move(11)
                # Player method2
                currentPlayer = input("Please enter your name: ")
                player1 = Player(Game)
                game = Game()
                infoReturned = game.player_vs_computer(player1, Intelligence)

                # Player method2

            elif option == 2:
                print(">> Player vs Player <<\n")
                print(">> Player 1 <<")
                name1 = input("Enter your name: ")
                if name1 == "":
                    print("You must enter a name.")                      
                else:
                    change_name = input("Are you sure you want to use "
                                        + "this name? Yes or no: ")
                    if change_name.lower() == "yes":
                        player1 = Player(name1, 0)
                        print(f"Welcome {name1}!")
                    elif change_name.lower() == "no":
                        print("Please enter a new name.")
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        break

                print(">> Player 2 <<")
                name2 = input("Enter your name: ")
                if name2 == "":
                    print("You must enter a name.")
                else:
                    change_name = input("Are you sure you want to use "
                                        + "this name? Yes or no: ")
                    if change_name.lower() == "yes":
                        player2 = Player(name2, 0)
                        print(f"Welcome {name2}!")
                    elif change_name.lower() == "no":
                        continue
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        break
                game = Game()
               
                winner = game.player_vs_player(player1, player2)

            elif option == 3:
                try:
                    print(">> Highscore <<\n")
                    highscore = HighScore()
                    highscore.save_score(winner)
                    # show_score = highscore.load_score()
                    # print(show_score)
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
                print(the_rules.show_rules())
                back_to_the_menu = int(input("Enter 0 to go back to the menu: "))
                if back_to_the_menu == 0:
                    print("Back to the menu.")

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
