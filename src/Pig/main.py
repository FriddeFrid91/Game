def main():
    import cmd
<<<<<<< HEAD
    from Intelligence import Intelligence
    from Dice import Dice
    from Rules import Rules
    from DiceHand import DiceHand
=======
>>>>>>> FriddeFrid_branch
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

<<<<<<< HEAD
        playersName2 = input("Please enter your name (Player 2): ")
        print(f"You entered: {playersName2}")
        player2 = Player("Player 2")
        player2.score = 0
        player2.createPlayer(playersName2)
        dictOfPlayers[playersName2] = 0
        dictOfPlayers[player2.name] = player2.score
        print(dictOfPlayers.values())

        option = int(input("Please enter a option: \n"))

        while True:
            print(">> Player vs player <<\n")
=======
        try:
            option = int(input("Please enter an option: "))
            
>>>>>>> FriddeFrid_branch
            if option == 1:
                print(">> Player vs Computer <<\n")
                # Implement one-player mode here

            elif option == 2:
<<<<<<< HEAD
                print(">> Player vs computer <<\n")
                Intelligence.intelligence_move()
                Intelligence.move()
                rolltheDice = int(input("Players turn - please enter 0 to roll"
                                        + " the dice. "))
                
=======
                print(">> Player vs Player <<\n")
                playersName1 = input("Please enter your name (Player 1): ")
                player1 = Player(playersName1)
                playersName2 = input("Please enter your name (Player 2): ")
                player2 = Player(playersName2)
                newGame = Game()
                newGame.PlayerVsPlayer(player1, player2, listOfPoints)
>>>>>>> FriddeFrid_branch
                
            elif option == 3:
                print(">> Highscore <<\n")
                # Implement highscore display

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
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
