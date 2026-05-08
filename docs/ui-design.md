# UI Module Design Document

## Overview
The ui.py module provides user-friendly interface functions for the Tic-Tac-Toe game.

## Functions

### display_welcome()
Prints game instructions to help players understand how to play.

### display_board(board)
Renders the current board state with:
- Column labels (1-3) at the top
- Row labels (1-3) on the left
- Clear visual separators (| and -)
- Empty squares displayed as spaces

### get_player_move(board, player)
Prompts the current player for a move with:
- Input format: "row column" (e.g., "1 3")
- Input validation with helpful error messages
- Range checking (1-3)
- Duplicate move detection
- Returns 0-indexed (row, col) tuple

### display_winner(winner)
Shows the game result:
- "X wins!" or "O wins!" for winner
- "It's a draw!" for draw

### play_again()
Asks players if they want to restart:
- Accepts "yes"/"y" or "no"/"n"
- Returns True/False

## Implementation Notes
- All user-facing numbering uses 1-3
- Internal board indexing uses 0-2
- Input validation handles non-numeric, out-of-range, and occupied square errors
