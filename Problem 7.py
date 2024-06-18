def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board, mark):
    # Check rows, columns and diagonals
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    return [mark, mark, mark] in win_conditions

def is_draw(board):
    return all(spot in ['X', 'O'] for spot in board)

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    players = []
    
    print("Welcome to Tic-Tac-Toe!")
    players.append(input("Enter name for Player 1 (X): "))
    players.append(input("Enter name for Player 2 (O): "))
    
    current_player = 0
    
    while True:
        print_board(board)
        print(f"{players[current_player]}'s turn ({'X' if current_player == 0 else 'O'})")
        
        move = -1
        while move not in range(9) or board[move] != ' ':
            try:
                move = int(input("Enter your move (0-8): "))
                if board[move] != ' ':
                    print("This spot is already taken. Choose another spot.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 0 and 8.")
        
        board[move] = 'X' if current_player == 0 else 'O'
        
        if check_winner(board, 'X' if current_player == 0 else 'O'):
            print_board(board)
            print(f"Congratulations! {players[current_player]} wins!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 1 - current_player

if __name__ == "__main__":
    tic_tac_toe()
