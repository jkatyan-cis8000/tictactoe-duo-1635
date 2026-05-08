"""
Tic-Tac-Toe Game Engine Module

Provides core game logic including board management, move validation,
win detection, and draw checking.
"""


def create_board():
    """Create and return a new 3x3 empty board."""
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]


def display_board(board):
    """Return a string representation of the current board state."""
    lines = []
    lines.append("   1   2   3")
    lines.append("  -----------")
    for i, row in enumerate(board):
        row_label = i + 1
        lines.append(f"{row_label} | {cell_display(row[0])} | {cell_display(row[1])} | {cell_display(row[2])} |")
        if i < 2:
            lines.append("  |---|---|---|")
    lines.append("  -----------\n")
    return "\n".join(lines)


def cell_display(cell):
    """Return display character for a cell (None, 'X', or 'O')."""
    return cell if cell is not None else ' '


def is_valid_move(board, row, col):
    """Check if a move at (row, col) is valid.
    
    Args:
        board: 3x3 list representing the game board
        row: Row index (0-2)
        col: Column index (0-2)
    
    Returns:
        True if the cell is empty, False otherwise
    """
    if not (0 <= row <= 2 and 0 <= col <= 2):
        return False
    return board[row][col] is None


def make_move(board, row, col, player):
    """Place a player's mark on the board.
    
    Args:
        board: 3x3 list representing the game board
        row: Row index (0-2)
        col: Column index (0-2)
        player: 'X' or 'O'
    
    Returns:
        Updated board with the move applied, or None if invalid
    """
    if not is_valid_move(board, row, col):
        return None
    
    new_board = [row[:] for row in board]  # Create a copy
    new_board[row][col] = player
    return new_board


def check_winner(board):
    """Check for a winner in the current board state.
    
    Returns:
        'X' if X wins, 'O' if O wins, None if no winner yet
    """
    # Check rows
    for row in board:
        if row[0] is not None and row[0] == row[1] == row[2]:
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] is not None and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    
    # Check diagonals
    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None


def is_board_full(board):
    """Check if the board is completely filled.
    
    Returns:
        True if all cells are occupied, False otherwise
    """
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True


def get_available_moves(board):
    """Get list of all available (empty) moves.
    
    Returns:
        List of (row, col) tuples for empty cells
    """
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                moves.append((row, col))
    return moves
