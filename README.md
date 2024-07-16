# Tic-tac-toe
This is my first mini game - project in python.
Board Representation: The game board is typically represented as a 3x3 list of characters. Empty spaces are marked with blanks (' '), 'X' for player 1, and 'O' for player 2.

Game Functions:

create_board(): Initializes an empty board.
print_board(board): Displays the current state of the board.
is_valid_move(board, move): Checks if a specific move is valid (empty space).
make_move(board, player, move): Places the player's mark on the board at the specified move.
has_won(board, player): Checks if a player has achieved a winning condition (three in a row horizontally, vertically, or diagonally).
is_draw(board): Checks if the board is full and no winner has emerged (a tie).
Game Loop: The core logic involves a loop that alternates between players. In each turn:

The current board is displayed.
The player chooses a valid move (can be a numerical position or a coordinate system).
The move is made on the board.
The game checks for a win or draw using the respective functions.
The loop continues until a winner is found or the board is full.
