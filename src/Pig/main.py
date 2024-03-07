def main():
<<<<<<< HEAD

    import cmd  
    from Intelligence import Intelligence
=======
    import cmd
    from Intelligence import Intelligence
    from Rules import Rules
<<<<<<< HEAD
=======
    from DiceHand import DiceHand
>>>>>>> 71d83f8ff91b7e87e1a5033719d30a50bb311ba5
>>>>>>> 90465df7123d75efbc0b19e5a0d21b914a444beb
    from Player import Player
    from Game import Game
    from Rules import Rules
    import sys

    dictPlayersScore = {}
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
<<<<<<< HEAD
            
=======
           
>>>>>>> 71d83f8ff91b7e87e1a5033719d30a50bb311ba5
            if option == 1:
                print(">> Player vs Computer <<\n")
<<<<<<< HEAD
                # enspelare mot datorn
=======
                Intelligence = Intelligence()
                Intelligence.intelligence_move()
                Intelligence.move()
                # Implement one-player mode here
>>>>>>> 90465df7123d75efbc0b19e5a0d21b914a444beb

            elif option == 2:
                print(">> Player vs Player <<\n")
                playersName1 = input("Please enter your name (Player 1): ")
                player1 = Player(playersName1)
                playersName2 = input("Please enter your name (Player 2): ")
                player2 = Player(playersName2)
                newGame = Game()
<<<<<<< HEAD
                newGame.PlayerVsPlayer(player1, player2)
=======
                newGame.PlayerVsPlayer(player1, player2, listOfPoints)
<<<<<<< HEAD
                
=======
>>>>>>> 90465df7123d75efbc0b19e5a0d21b914a444beb
               
>>>>>>> 71d83f8ff91b7e87e1a5033719d30a50bb311ba5
            elif option == 3:
                print(">> Highscore <<\n")
                # Implement highscore display

            elif option == 4:
                print(">> Rules <<\n")
                theRules = Rules()
                theRules.showRules()
                backToMenu = int(input("Enter 0 to go back to the main menu: "))
                if backToMenu == 0:
                    print("Going back to the main menu.")
                else:
                    print("Invalid input. Please enter 0 to go back to the main menu.")

            elif option == 5:
                print("Goodbye!")
                sys.exit()

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
