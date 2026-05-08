def create_board():
    return [[None for _ in range(3)] for _ in range(3)]


def display_board(board):
    lines = []
    for row in board:
        cells = [cell if cell is not None else ' ' for cell in row]
        lines.append(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    return "\n---|---|---\n".join(lines)


def is_valid_move(board, row, col):
    if not (0 <= row < 3 and 0 <= col < 3):
        return False
    return board[row][col] is None


def make_move(board, row, col, player):
    new_board = [row[:] for row in board]
    new_board[row][col] = player
    return new_board


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None


def is_board_full(board):
    return all(cell is not None for row in board for cell in row)


def get_available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] is None]
