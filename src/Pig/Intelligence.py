class Intelligence:
    """Intelligence class"""
    def __init__(self):
        self.score = 0


    def intelligence_move(self):
        """Intelligence move"""
        roundScore = 0
        while roundScore < 100:
            roll = self.rollTheDice()
            print(f"Intelligence rolled a {roll}. Total score: {roundScore}")
            if roll == 1:
                roundScore = 0
                print(f"Intelligence rolled a 1. Total score: {roundScore}")
                print
            roundScore += roll
            if roundScore >= 100:
                print("Intelligence wins!")
                break


    def move(self):
        """Player move"""
        player = input("Enter your name: ")
        roundScore = 0
        while roundScore < 100:
            roll = self.rollTheDice()
            print(f"You rolled a {roll}. Total score: {roundScore}")
            if roll == 1:
                roundScore = 0
                print(f"You rolled a 1. Total score: {roundScore}")
            roundScore += roll
            if roundScore >= 100:
                print(f"{player} wins!")
                break
