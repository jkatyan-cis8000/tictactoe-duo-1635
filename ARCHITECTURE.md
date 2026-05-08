# Tic-Tac-Toe Architecture

## Overview
A two-player Tic-Tac-Toe game with a 3x3 grid, turn tracking, and win/draw detection.

## Modules

### 1. game_engine.py
**Responsibility**: Core game logic and state management

**Functions**:
- `create_board()` - Initialize empty 3x3 grid
- `display_board(board)` - Show current board state
- `is_valid_move(board, row, col)` - Check if move is valid
- `make_move(board, row, col, player)` - Place X or O
- `check_winner(board)` - Check for win conditions (rows, cols, diagonals)
- `is_board_full(board)` - Check for draw
- `get_available_moves(board)` - List valid moves

**Interfaces**:
- Board format: 3x3 list of lists (None, 'X', or 'O')
- Player representation: 'X' (first) or 'O' (second)

### 2. ui.py
**Responsibility**: User interface and interaction

**Functions**:
- `displayWelcome()` - Show game instructions
- ` getPlayerMove(board, player)` - Get and validate player input
- `displayBoard(board)` - Render the grid with row/column labels
- `displayWinner(winner)` - Show win message or draw
- `playAgain()` - Ask to restart game

**Interface Requirements**:
- Clear numbering: rows 1-3, columns 1-3
- Input validation with helpful error messages
- Visual board representation with separators

### 3. main.py (Shared)
**Responsibility**: Game loop coordination

**Flow**:
1. Initialize game state
2. Loop until win or draw:
   - Display board
   - Get player move
   - Update board
   - Check for winner
   - Switch player
3. Display final result
4. Offer replay

## File Ownership
- **Player 1 (Agent X)**: game_engine.py + main.py coordination
- **Player 2 (Agent O)**: ui.py + main.py coordination

## Dependencies
- ui depends on game_engine for board state
- main depends on both modules
