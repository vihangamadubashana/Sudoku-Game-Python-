# validate_input.py

import tkinter as tk


def validate_input(gui, row: int, col: int):
    """
    Validate user input in a Sudoku cell.

    :param gui: Instance of SudokuGUI (from gui.py).
    :param row: Row index (0–8).
    :param col: Column index (0–8).
    """
    cell = gui.cells[row][col]
    value = cell.get().strip()

    # Skip validation if the cell was part of the original puzzle (disabled state)
    if cell.cget("state") == "disabled":
        return

    # Empty cell
    if value == "":
        gui.board.grid[row][col] = 0
        cell.config(bg="white")
        return

    # Invalid input (non-digit or outside 1–9)
    if not value.isdigit() or not (1 <= int(value) <= 9):
        cell.delete(0, tk.END)
        cell.config(bg="red")
        return

    # Valid number check against Sudoku rules
    num = int(value)
    if gui.board.is_valid(row, col, num):
        gui.board.grid[row][col] = num
        cell.config(bg="white")
        gui.check_progress(row, col)
    else:
        # Wrong placement → red highlight
        cell.config(bg="red")
