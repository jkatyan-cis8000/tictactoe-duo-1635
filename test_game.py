"""
Tests for Tic-Tac-Toe game engine.
"""

import unittest
from game_engine import create_board, display_board, is_valid_move, make_move
from game_engine import check_winner, is_board_full, get_available_moves


class TestCreateBoard(unittest.TestCase):
    """Tests for create_board function."""
    
    def test_creates_3x3_board(self):
        """Board should be 3x3."""
        board = create_board()
        self.assertEqual(len(board), 3)
        for row in board:
            self.assertEqual(len(row), 3)
    
    def test_all_cells_empty(self):
        """All cells should be None initially."""
        board = create_board()
        for row in board:
            for cell in row:
                self.assertIsNone(cell)


class TestIsValidMove(unittest.TestCase):
    """Tests for is_valid_move function."""
    
    def test_valid_moves(self):
        """All cells should be valid on empty board."""
        board = create_board()
        for row in range(3):
            for col in range(3):
                self.assertTrue(is_valid_move(board, row, col))
    
    def test_invalid_out_of_bounds(self):
        """Moves outside 0-2 range should be invalid."""
        board = create_board()
        self.assertFalse(is_valid_move(board, -1, 0))
        self.assertFalse(is_valid_move(board, 0, -1))
        self.assertFalse(is_valid_move(board, 3, 0))
        self.assertFalse(is_valid_move(board, 0, 3))
    
    def test_invalid_occupied_cell(self):
        """Moves on occupied cells should be invalid."""
        board = create_board()
        board[1][1] = 'X'
        self.assertFalse(is_valid_move(board, 1, 1))


class TestMakeMove(unittest.TestCase):
    """Tests for make_move function."""
    
    def test_valid_move(self):
        """Valid move should place player mark."""
        board = create_board()
        result = make_move(board, 1, 1, 'X')
        self.assertIsNotNone(result)
        self.assertEqual(result[1][1], 'X')
        # Original board should be unchanged
        self.assertIsNone(board[1][1])
    
    def test_invalid_move_returns_none(self):
        """Invalid move should return None."""
        board = create_board()
        board[1][1] = 'X'
        result = make_move(board, 1, 1, 'O')
        self.assertIsNone(result)
    
    def test_move_on_occupied_cell(self):
        """Cannot place mark on occupied cell."""
        board = create_board()
        board[0][0] = 'X'
        result = make_move(board, 0, 0, 'O')
        self.assertIsNone(result)


class TestCheckWinner(unittest.TestCase):
    """Tests for check_winner function."""
    
    def test_row_win_x(self):
        """X wins with row."""
        board = [['X', 'X', 'X'],
                 [None, None, None],
                 [None, None, None]]
        self.assertEqual(check_winner(board), 'X')
    
    def test_row_win_o(self):
        """O wins with row."""
        board = [[None, None, None],
                 ['O', 'O', 'O'],
                 [None, None, None]]
        self.assertEqual(check_winner(board), 'O')
    
    def test_col_win_x(self):
        """X wins with column."""
        board = [['X', None, None],
                 ['X', None, None],
                 ['X', None, None]]
        self.assertEqual(check_winner(board), 'X')
    
    def test_col_win_o(self):
        """O wins with column."""
        board = [[None, 'O', None],
                 [None, 'O', None],
                 [None, 'O', None]]
        self.assertEqual(check_winner(board), 'O')
    
    def test_diag_win_x(self):
        """X wins with diagonal (top-left to bottom-right)."""
        board = [['X', None, None],
                 [None, 'X', None],
                 [None, None, 'X']]
        self.assertEqual(check_winner(board), 'X')
    
    def test_diag_win_o(self):
        """O wins with diagonal (top-right to bottom-left)."""
        board = [[None, None, 'O'],
                 [None, 'O', None],
                 ['O', None, None]]
        self.assertEqual(check_winner(board), 'O')
    
    def test_no_winner(self):
        """Return None when no winner."""
        board = create_board()
        self.assertIsNone(check_winner(board))
        
        board[0][0] = 'X'
        board[1][1] = 'O'
        board[2][2] = 'X'
        self.assertIsNone(check_winner(board))


class TestIsBoardFull(unittest.TestCase):
    """Tests for is_board_full function."""
    
    def test_empty_not_full(self):
        """Empty board is not full."""
        board = create_board()
        self.assertFalse(is_board_full(board))
    
    def test_full_board(self):
        """Completely filled board is full."""
        board = [['X', 'O', 'X'],
                 ['O', 'X', 'O'],
                 ['X', 'O', 'X']]
        self.assertTrue(is_board_full(board))
    
    def test_partial_not_full(self):
        """Board with empty cells is not full."""
        board = [['X', 'O', 'X'],
                 ['O', None, 'O'],
                 ['X', 'O', 'X']]
        self.assertFalse(is_board_full(board))


class TestGetAvailableMoves(unittest.TestCase):
    """Tests for get_available_moves function."""
    
    def test_all_moves_available(self):
        """Empty board has all 9 moves available."""
        board = create_board()
        moves = get_available_moves(board)
        self.assertEqual(len(moves), 9)
    
    def test_some_moves_occupied(self):
        """Occupied cells should not be in available moves."""
        board = create_board()
        board[1][1] = 'X'
        moves = get_available_moves(board)
        self.assertEqual(len(moves), 8)
        self.assertNotIn((1, 1), moves)


if __name__ == '__main__':
    unittest.main()
