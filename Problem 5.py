import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"

def play_round():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while player_choice not in ["rock", "paper", "scissors"]:
        player_choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(player_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win this round!")
    else:
        print("Computer wins this round!")
    
    return winner

def play_game():
    player_wins = 0
    computer_wins = 0

    while player_wins < 2 and computer_wins < 2:
        winner = play_round()
        if winner == "player":
            player_wins += 1
        elif winner == "computer":
            computer_wins += 1
        
        print(f"Score: Player {player_wins} - Computer {computer_wins}\n")

    if player_wins == 2:
        print("Congratulations! You won the game!")
    else:
        print("Sorry, the computer won the game.")

play_game()
