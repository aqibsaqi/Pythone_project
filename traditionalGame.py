import random
import numpy as np

# Matrix representing the game outcome
# [Rock, Paper, Scissors] rows = user choices, columns = computer choices
outcome_matrix = np.array([
    [0, -1, 1],  # Rock vs (Rock, Paper, Scissors)
    [1, 0, -1],  # Paper vs (Rock, Paper, Scissors)
    [-1, 1, 0]   # Scissors vs (Rock, Paper, Scissors)
])

choices = ['rock', 'paper', 'scissors']

def get_user_choice():
    """Get the user's choice."""
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in choices:
            return choices.index(choice)  # Return the index of the choice
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")

def get_computer_choice():
    """Randomly select the computer's choice."""
    return random.choice([0, 1, 2])  # Return a random index for the computer

def determine_winner(user_choice, computer_choice):
    """Determine the winner using the outcome matrix."""
    result = outcome_matrix[user_choice, computer_choice]
    if result == 0:
        return "It's a tie!"
    elif result == 1:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Play the rock, paper, scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYour choice: {choices[user_choice]}")
    print(f"Computer's choice: {choices[computer_choice]}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
