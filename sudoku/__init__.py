# Marks sudoku as a package
from .core import SudokuBoard
from .solver import solve
from .generator import generate_puzzle

__all__ = ["SudokuBoard", "solve", "generate_puzzle"]
