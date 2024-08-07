import random

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def check_tie(board):
    return ' ' not in board

def get_computer_move(board):
    return random.choice([i for i, cell in enumerate(board) if cell == ' '])

def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'
    mode = input("Choose game mode - (1) Player vs Player, (2) Player vs Computer: ") == '2'

    while True:
        print_board(board)
        if current_player == 'O' and mode:
            move = get_computer_move(board)
            print(f"Computer chooses position {move + 1}")
        else:
            try:
                move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
                if not (0 <= move < 9) or board[move] != ' ':
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")
                continue
        
        board[move] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()