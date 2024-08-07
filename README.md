
# Tic-Tac-Toe Game

This repository contains a simple implementation of the classic Tic-Tac-Toe game in Python. The game can be played in two modes: Player vs Player and Player vs Computer.

## How to Play

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/tic-tac-toe.git
    cd tic-tac-toe
    ```

2. Run the game:
    ```sh
    python tic_tac_toe.py
    ```

## Game Modes

- **Player vs Player**: Two human players take turns to mark the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
- **Player vs Computer**: The player competes against the computer. The computer makes random valid moves.

## Code Overview

### Functions

- `print_board(board)`: Prints the current state of the board.
- `check_win(board, player)`: Checks if the given player has won.
- `check_tie(board)`: Checks if the game is a tie.
- `get_computer_move(board)`: Returns a random valid move for the computer.
- `tic_tac_toe()`: The main function to start the game.

### Example Usage

1. The game starts by asking the user to choose a game mode: Player vs Player or Player vs Computer.
2. Players take turns to enter their move (position 1-9).
3. The game continues until there is a win or a tie.

### Sample Output

```sh
Choose game mode - (1) Player vs Player, (2) Player vs Computer: 2
   |   |   
-----------
   |   |   
-----------
   |   |   
Player X, enter a position (1-9): 1
 X |   |   
-----------
   |   |   
-----------
   |   |   
Computer chooses position 7
 X |   |   
-----------
   |   |   
-----------
 O |   |   
Player X, enter a position (1-9): 2
 X | X |   
-----------
   |   |   
-----------
 O |   |
Computer chooses position 3
 X | X | O
-----------
   |   |
-----------
 O |   |
Player X, enter a position (1-9): 9
 X | X | O
-----------
   |   |
-----------
 O |   | X
Computer chooses position 4
 X | X | O
-----------
 O |   |
-----------
 O |   | X
Player X, enter a position (1-9): 5
 X | X | O
-----------
 O | X |
-----------
 O |   | X
Player X wins!
...
```

## Requirements

- Python 3.x

## License

This project is licensed 

## Contributing

Feel free to submit issues and pull requests for new features, improvements, and bugs. Contributions are welcome!

