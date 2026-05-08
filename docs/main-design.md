# Main Game Loop Design Document

## Overview
The main.py module coordinates the Tic-Tac-Toe game flow by integrating game_engine and ui modules.

## Game Flow
1. Display welcome message
2. Initialize new game board
3. Set current player to 'X'
4. Loop until win or draw:
   - Display current board
   - Get player move with validation
   - Update board with move
   - Check for winner
   - Check for draw (board full)
   - Switch player
5. Display final result
6. Ask to play again
7. Repeat or exit

## Integration Points
- **game_engine**: create_board, make_move, check_winner, is_board_full
- **ui**: display_welcome, display_board, get_player_move, display_winner, play_again

## Player Turn Management
- Player X always starts
- Turns alternate after each valid move
- Loop continues until check_winner returns non-None or board is full
