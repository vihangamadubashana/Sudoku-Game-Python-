import tkinter as tk
from sudoku.core import SudokuBoard
from sudoku.generator import generate_puzzle
from sudoku.solver import solve


class SudokuGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sudoku Game")
        self.board = generate_puzzle()
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.draw_board()
        self.add_buttons()

    def draw_board(self):
        board_frame = tk.Frame(self.root, bg="black")
        board_frame.pack(padx=10, pady=10)

        # Create 3×3 block frames with thick border
        block_frames = [[None for _ in range(3)] for _ in range(3)]
        for br in range(3):
            for bc in range(3):
                block = tk.Frame(
                    board_frame,
                    highlightbackground="black",
                    highlightthickness=2,  # Thick border for block
                    bd=0
                )
                block.grid(row=br, column=bc, padx=2, pady=2)
                block_frames[br][bc] = block

        # Place entries inside correct block
        for row in range(9):
            for col in range(9):
                block_row, block_col = row // 3, col // 3
                block = block_frames[block_row][block_col]

                entry = tk.Entry(
                    block,
                    width=2,
                    font=("Arial", 18),
                    justify="center",
                    relief="solid",
                    borderwidth=1  # Thin border for cell
                )
                entry.grid(row=row % 3, column=col % 3, padx=1, pady=1)

                if self.board.grid[row][col] != 0:
                    entry.insert(0, str(self.board.grid[row][col]))
                    entry.config(state="disabled", disabledforeground="black")
                else:
                    entry.bind("<FocusOut>", lambda e, r=row, c=col: self.validate_input(r, c))

                self.cells[row][col] = entry

    def add_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        solve_btn = tk.Button(button_frame, text="Solve", command=self.solve_puzzle)
        solve_btn.grid(row=0, column=0, padx=5)

        reset_btn = tk.Button(button_frame, text="New Game", command=self.new_game)
        reset_btn.grid(row=0, column=1, padx=5)

    def validate_input(self, row, col):
        """Validate user input for a cell"""
        value = self.cells[row][col].get().strip()

        if value == "":
            self.board.grid[row][col] = 0
            self.cells[row][col].config(bg="white")
            return

        if not value.isdigit() or not (1 <= int(value) <= 9):
            self.cells[row][col].delete(0, tk.END)
            self.cells[row][col].config(bg="red")
            return

        num = int(value)
        if self.board.is_valid(row, col, num):
            self.board.grid[row][col] = num
            self.cells[row][col].config(bg="white")
            self.check_progress(row, col)
        else:
            self.cells[row][col].config(bg="red")

    def check_progress(self, row, col):
        """Highlight row/col/3x3 if completed correctly"""
        # Row
        if all(self.board.grid[row][c] != 0 for c in range(9)) and \
           len(set(self.board.grid[row])) == 9:
            for c in range(9):
                self.cells[row][c].config(bg="lightgreen")

        # Column
        col_vals = [self.board.grid[r][col] for r in range(9)]
        if all(val != 0 for val in col_vals) and len(set(col_vals)) == 9:
            for r in range(9):
                self.cells[r][col].config(bg="lightgreen")

        # 3x3 block
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        block_vals = []
        for r in range(start_row, start_row+3):
            for c in range(start_col, start_col+3):
                block_vals.append(self.board.grid[r][c])

        if all(val != 0 for val in block_vals) and len(set(block_vals)) == 9:
            for r in range(start_row, start_row+3):
                for c in range(start_col, start_col+3):
                    self.cells[r][c].config(bg="lightgreen")

    def solve_puzzle(self):
        solve(self.board)
        for row in range(9):
            for col in range(9):
                self.cells[row][col].config(state="normal")
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].insert(0, str(self.board.grid[row][col]))
                self.cells[row][col].config(state="disabled", disabledforeground="blue")

    def new_game(self):
        self.board = generate_puzzle()
        for row in range(9):
            for col in range(9):
                self.cells[row][col].config(state="normal", bg="white")
                self.cells[row][col].delete(0, tk.END)
                if self.board.grid[row][col] != 0:
                    self.cells[row][col].insert(0, str(self.board.grid[row][col]))
                    self.cells[row][col].config(state="disabled", disabledforeground="black")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    gui = SudokuGUI()
    gui.run()
