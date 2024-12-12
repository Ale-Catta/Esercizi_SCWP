import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the round."""
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    """Play a single round of rock-paper-scissors."""
    print("Welcome to Rock-Paper-Scissors!")
    
    player_wins = 0
    computer_wins = 0
    
    while True:
        # Get the player's choice
        player_choice = input("Enter your choice (rock, paper, or scissors), or type 'exit' to quit: ").lower()
        
        if player_choice == "exit":
            break
        
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input, please choose rock, paper, or scissors.")
            continue
        
        # Get the computer's choice
        computer_choice = get_computer_choice()
        print(f"The computer chose: {computer_choice}")
        
        # Determine the winner
        winner = determine_winner(player_choice, computer_choice)
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win this round!")
            player_wins += 1
        else:
            print("Computer wins this round!")
            computer_wins += 1
        
        print(f"Current score -> Player: {player_wins}, Computer: {computer_wins}")
    
    # End of game
    print("\nGame over!")
    print(f"Final score -> Player: {player_wins}, Computer: {computer_wins}")
    
if __name__ == "__main__":
    play_game()