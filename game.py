import random
class Game:
    HANDS = ("ROCK", "SCISSORS", "PAPER")
    def __init__(self, max_score = 3):
        self.player_score = 0
        self.computer_score = 0
        self.max_score = max_score
    def play(self):
        self.__print_score()
        while self.__is_game_running():
            print(f"Possible hands: {', '.join(self.HANDS)}")
            player_hand = input("What do you choose?\n> ")
            if player_hand not in self.HANDS:
                print("Wrong input. Please try again")
                continue
            computer_hand = random.choice(self.HANDS)
            print(f"Computer played {computer_hand}")
            self.__compare_hands(player_hand, computer_hand)
            self.__print_score()
        self.__print_game_over()
    def __is_game_running(self):
        return self.player_score < self.max_score \
            and self.computer_score < self.max_score
    def __compare_hands(self, player_hand, computer_hand):
        if player_hand == computer_hand:
            print("Draw!")
        elif any([
            player_hand == "ROCK" and computer_hand == "SCISSORS",
            player_hand == "PAPER" and computer_hand == "ROCK",
            player_hand == "SCISSORS" and computer_hand == "PAPER"
            ]):
            self.player_score += 1
            print("You win this one")
        # elif (1 + self.HANDS.index(player_hand)) % 3 < (1 + self.HANDS.index(computer_hand)) % 3:
        #     self.player_score +=1
        #     print("You win this one")
        else:
            self.computer_score += 1
            print("You lose this one")
    def __print_score(self):
        print(f"Player score: {self.player_score} - Computer score: {self.computer_score}")
    def __print_game_over(self):
        if self.player_score > self.computer_score:
            print("Player won")
        else:
            print("Computer won")
game = Game()
game.play()