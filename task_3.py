import random

def get_user_choice():
    """Get user's choice for Rock, Paper, or Scissors"""
    while True:
        user_choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice! Please enter Rock, Paper, or Scissors.")

def get_daya_choice():
    """Generate the daya's choice for Rock, Paper, or Scissors"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, daya_choice):
    """Determine the winner of the game"""
    print(f"daya chose {daya_choice}")
    if user_choice == daya_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and daya_choice == "scissors") or
        (user_choice == "paper" and daya_choice == "rock") or
        (user_choice == "scissors" and daya_choice == "paper")
    ):
        return "You win!"
    else:
        return "Daya wins!"

def play_game():
    """Play a round of Rock, Paper, Scissors"""
    print("Let's play Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    daya_choice = get_daya_choice()
    result = determine_winner(user_choice, daya_choice)
    print(result)

if __name__ == "__main__":
    play_game()
