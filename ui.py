def display_welcome():
    print("Welcome to Tic-Tac-Toe!")
    print("\nInstructions:")
    print("1. The game is played on a 3x3 grid")
    print("2. Players take turns placing 'X' or 'O' on the board")
    print("3. To make a move, enter row and column numbers (1-3)")
    print("4. First player to get 3 in a row (horizontally, vertically, or diagonally) wins")
    print("5. If all squares are filled with no winner, the game is a draw")
    print()


def display_board(board):
    print("\n   1   2   3")
    print("  -----------")
    for i, row in enumerate(board):
        row_label = i + 1
        print(f"{row_label} | {row[0] if row[0] else ' '} | {row[1] if row[1] else ' '} | {row[2] if row[2] else ' '} |")
        if i < 2:
            print("  |---|---|---|")
    print("  -----------\n")


def get_player_move(board, player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row column): ")
            parts = move.strip().split()
            
            if len(parts) != 2:
                print("Invalid input. Please enter two numbers: row column (e.g., '1 3')")
                continue
            
            row_str, col_str = parts
            row = int(row_str)
            col = int(col_str)
            
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Invalid input. Row and column must be between 1 and 3.")
                continue
            
            if board[row - 1][col - 1] is not None:
                print("That square is already taken. Please choose an empty square.")
                continue
            
            return (row - 1, col - 1)
        except ValueError:
            print("Invalid input. Please enter valid numbers for row and column (1-3).")


def display_winner(winner):
    if winner == 'draw':
        print("It's a draw!")
    else:
        print(f"{winner} wins!")


def play_again():
    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        if answer in ['yes', 'y']:
            return True
        elif answer in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")
