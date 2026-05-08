import unittest
import sys
sys.path.insert(0, '/workspace/tictactoe-duo-1635/src')
from game_engine import create_board, display_board, is_valid_move, make_move, check_winner, is_board_full, get_available_moves


class TestTicTacToe(unittest.TestCase):
    
    def test_create_board(self):
        board = create_board()
        self.assertEqual(len(board), 3)
        for row in board:
            self.assertEqual(len(row), 3)
            for cell in row:
                self.assertIsNone(cell)
    
    def test_display_board(self):
        board = create_board()
        display = display_board(board)
        self.assertIn("   |   |   ", display)
        self.assertIn("---|---|---", display)
    
    def test_is_valid_move_valid(self):
        board = create_board()
        self.assertTrue(is_valid_move(board, 0, 0))
        self.assertTrue(is_valid_move(board, 1, 1))
        self.assertTrue(is_valid_move(board, 2, 2))
    
    def test_is_valid_move_invalid(self):
        board = create_board()
        board[0][0] = 'X'
        self.assertFalse(is_valid_move(board, 0, 0))
        self.assertFalse(is_valid_move(board, -1, 0))
        self.assertFalse(is_valid_move(board, 3, 0))
        self.assertFalse(is_valid_move(board, 0, -1))
        self.assertFalse(is_valid_move(board, 0, 3))
    
    def test_make_move(self):
        board = create_board()
        new_board = make_move(board, 0, 0, 'X')
        self.assertEqual(new_board[0][0], 'X')
        self.assertIsNone(board[0][0])
    
    def test_check_winner_rows(self):
        board = create_board()
        board[0] = ['X', 'X', 'X']
        self.assertEqual(check_winner(board), 'X')
        
        board = create_board()
        board[1] = ['O', 'O', 'O']
        self.assertEqual(check_winner(board), 'O')
    
    def test_check_winner_columns(self):
        board = create_board()
        for i in range(3):
            board[i][0] = 'X'
        self.assertEqual(check_winner(board), 'X')
        
        board = create_board()
        for i in range(3):
            board[i][1] = 'O'
        self.assertEqual(check_winner(board), 'O')
    
    def test_check_winner_diagonals(self):
        board = create_board()
        for i in range(3):
            board[i][i] = 'X'
        self.assertEqual(check_winner(board), 'X')
        
        board = create_board()
        for i in range(3):
            board[i][2-i] = 'O'
        self.assertEqual(check_winner(board), 'O')
    
    def test_check_winner_no_winner(self):
        board = create_board()
        board[0][0] = 'X'
        board[0][1] = 'O'
        board[0][2] = 'X'
        self.assertIsNone(check_winner(board))
        
        board = create_board()
        self.assertIsNone(check_winner(board))
    
    def test_is_board_full(self):
        board = create_board()
        self.assertFalse(is_board_full(board))
        
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
        self.assertTrue(is_board_full(board))
    
    def test_get_available_moves(self):
        board = create_board()
        moves = get_available_moves(board)
        self.assertEqual(len(moves), 9)
        
        board[0][0] = 'X'
        moves = get_available_moves(board)
        self.assertEqual(len(moves), 8)
        self.assertNotIn((0, 0), moves)
    
    def test_game_flow(self):
        board = create_board()
        board = make_move(board, 0, 0, 'X')
        board = make_move(board, 1, 1, 'O')
        board = make_move(board, 0, 1, 'X')
        board = make_move(board, 2, 2, 'O')
        board = make_move(board, 0, 2, 'X')
        
        self.assertEqual(check_winner(board), 'X')


if __name__ == '__main__':
    unittest.main()
