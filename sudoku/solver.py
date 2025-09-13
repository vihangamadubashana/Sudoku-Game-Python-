from sudoku.core import SudokuBoard

def solve(board: SudokuBoard):
    """Backtracking Sudoku solver"""
    for row in range(9):
        for col in range(9):
            if board.grid[row][col] == 0:
                for num in range(1, 10):
                    if board.is_valid(row, col, num):
                        board.grid[row][col] = num
                        if solve(board):
                            return True
                        board.grid[row][col] = 0
                return False
    return True
