#! python3


import random


class Game:

    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.p_score = 0
        self.c_score = 0

    def play(self):
        while True:
            p_choice = self.get_p_choice()
            if p_choice == 'quit':
                print("Thanks for playing! Final scores:")
                print(f"Player: {self.p_score}")
                print(f"Computer: {self.c_score}")
                break
            c_choice = self.get_c_choice()
            self.display_choices(p_choice, c_choice)
            self.determine_winner(p_choice, c_choice)

    def get_p_choice(self):
        while True:
            choice = input("Enter your choice (rock/paper/scissors/lizard/spock) or 'quit' to end the game: ").lower()
            if choice in self.choices or choice == 'quit':
                return choice
            else:
                print("Invalid input. Please choose from 'rock', 'paper', 'scissors', 'lizard', 'spock', or 'quit'.")

    def get_c_choice(self):
        return random.choice(self.choices)

    def display_choices(self, p_choice, c_choice):
        print(f"Player chooses {p_choice}")
        print(f"Computer chooses {c_choice}")

    def determine_winner(self, p_choice, c_choice):
        if p_choice == c_choice:
            print("It's a tie!")
        elif (p_choice == 'rock' and (c_choice == 'scissors' or c_choice == 'lizard')) or \
             (p_choice == 'paper' and (c_choice == 'rock' or c_choice == 'spock')) or \
             (p_choice == 'scissors' and (c_choice == 'paper' or c_choice == 'lizard')) or \
             (p_choice == 'lizard' and (c_choice == 'spock' or c_choice == 'paper')) or \
             (p_choice == 'spock' and (c_choice == 'scissors' or c_choice == 'rock')):
            print("Player wins!")
            self.p_score += 1
        else:
            print("Computer wins!")
            self.c_score += 1

if __name__ == "__main__":
    g = Game()
    g.play()