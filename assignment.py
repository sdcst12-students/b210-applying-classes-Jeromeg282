#! python3


import random


class game:


  def __init__(self, name):
    self.valid_moves = ["rock", "spock", "paper", "lizard", "scissors"]
    if name in self.valid_moves:
            self.player_choice = name
            self.computer_choice = random.choice(self.valid_moves)
    else:
            print("Invalid input. Please choose from: rock, spock, paper, lizard, or scissors.")
  def winnercheck(self):
        if self.player_choice == self.computer_choice:
            return "It's a tie"
        if (self.player_choice == "rock" and self.computer_choice in ["lizard", "scissors"]) or \
           (self.player_choice == "spock" and self.computer_choice in ["rock", "scissors"]) or \
           (self.player_choice == "paper" and self.computer_choice in ["spock", "rock"]) or \
           (self.player_choice == "lizard" and self.computer_choice in ["spock", "paper"]) or \
           (self.player_choice == "scissors" and self.computer_choice in ["lizard", "paper"]):
            return "You win"
        else:
            return "You lost"

  def play_game(self):
        print(f"Player's choice: {self.player_choice}")
        print(f"Computer's choice: {self.computer_choice}")
        print(self.winnercheck())






  pass


# This is the only command allowed that is not in the class template. All code must be done there.
g = game()
