import sys
sys.path.insert(0, 'src')

from game_engine import create_board, make_move, check_winner, is_board_full
from ui import display_welcome, display_board, get_player_move, display_winner, play_again


def main():
    display_welcome()
    
    while True:
        board = create_board()
        current_player = 'X'
        
        while True:
            display_board(board)
            row, col = get_player_move(board, current_player)
            board = make_move(board, row, col, current_player)
            
            winner = check_winner(board)
            if winner:
                display_board(board)
                display_winner(winner)
                break
            
            if is_board_full(board):
                display_board(board)
                display_winner('draw')
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
        
        if not play_again():
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()
