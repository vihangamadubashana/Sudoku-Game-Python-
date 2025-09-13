import random
from sudoku.core import SudokuBoard
from sudoku.solver import solve



def generate_puzzle(empty_cells=40):
    """Generate Sudoku puzzle by solving a board and removing cells"""
    board = SudokuBoard()
    fill_diagonal_boxes(board)
    solve(board)
    remove_numbers(board, empty_cells)
    return board

def fill_diagonal_boxes(board):
    """Fill 3 diagonal 3x3 boxes randomly"""
    for i in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for r in range(3):
            for c in range(3):
                board.grid[i+r][i+c] = nums.pop()

def remove_numbers(board, empty_cells):
    """Remove numbers to create puzzle"""
    count = 0
    while count < empty_cells:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board.grid[row][col] != 0:
            board.grid[row][col] = 0
            count += 1
