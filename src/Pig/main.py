from Game import Game
from Player import Player
from Rules import Rules
from HighScore import HighScore
from Intelligence import Intelligence


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
                print(">> Player 1 <<")
                name1 = ""
                while name1 == "":
                    try:
                        name1 = input("Enter your name: ")
                        if name1 == "":
                            print("You must enter a name.")
                            continue
                        change_name = input("Are you sure you want to use "
                                            + "this name? Yes or no: ")
                        if change_name.lower() == "yes":
                            player1 = Player(name1, 0)
                            print(f"Welcome {name1}!")
                        elif change_name.lower() == "no":
                            name1 = ""
                            print("Please enter a new name.")
                            continue
                        elif change_name.lower() != "yes" or change_name.lower() != "no":
                            print("Invalid input. Please enter a name: ")
                            name1 = ""
                            continue
                    except ValueError:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        continue

                print(">> Player 2 <<")
                name2 = ""
                while name2 == "":
                    try:
                        name2 = input("Enter your name: ")
                        if name2 == "":
                            print("You must enter a name.")
                            continue
                        change_name = input("Are you sure you want to use "
                                            + "this name? Yes or no: ")
                        if change_name.lower() == "yes":
                            player2 = Player(name2, 0)
                            print(f"Welcome {name2}!")
                        elif change_name.lower() == "no":
                            name2 = ""
                            print("Please enter a new name.")
                            continue
                        elif change_name.lower() != "yes" or change_name.lower() != "no":
                            print("Invalid input. Please enter a name: ")
                            name2 = ""
                            continue
                    except ValueError:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        break
                
                game = Game()
                winner = game.player_vs_player(player1, player2)

            elif option == 3:
                try:
                    highScore = HighScore()
                    highScore.load_score()
                    highScore.save_score(winner)
                    winner = None
                    back_to_menu = int(input("Enter to go back to the menu: "))
                    if back_to_menu == "":
                        print("Back to the menu.")
                    else:
                        print("Invalid input.")

                except UnboundLocalError:
                    winner = None
                    highScore.load_score()
                    highScore.save_score(winner)

            elif option == 4:
                print(">> Rules <<\n")
                the_rules = Rules("Rules of Pig")
                print(the_rules.show_rules())
                back_to_menu = int(input("Enter to go back to the menu: "))
                if back_to_menu == "":
                    print("Back to the menu.")
                else:
                    print("Invalid input.")

            elif option == 5:
                print("Goodbye!")
                break

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
