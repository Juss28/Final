import random

def roll_dice():
    return random.randint(1, 6)

def play_round():
    player1_roll = roll_dice()
    player2_roll = roll_dice()
    print(f"Player 1 rolled: {player1_roll}")
    print(f"Player 2 rolled: {player2_roll}")
    
    if player1_roll > player2_roll:
        print("Player 1 wins this round!\n")
        return 1
    elif player2_roll > player1_roll:
        print("Player 2 wins this round!\n")
        return 2
    else:
        print("This round is a tie!\n")
        return 0

def play_game():
    player1_wins = 0
    player2_wins = 0
    rounds_played = 0
    
    while player1_wins < 2 and player2_wins < 2 and rounds_played < 3:
        winner = play_round()
        rounds_played += 1
        
        if winner == 1:
            player1_wins += 1
        elif winner == 2:
            player2_wins += 1
    
    if player1_wins > player2_wins:
        print("Player 1 wins the game!")
    elif player2_wins > player1_wins:
        print("Player 2 wins the game!")
    else:
        print("The game is a tie!")

# Start the game
play_game()
