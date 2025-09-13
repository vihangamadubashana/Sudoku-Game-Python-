class SudokuBoard:
    def __init__(self, grid=None):
        if grid:
            self.grid = grid
        else:
            self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def is_valid(self, row, col, num):
        """Check if placing num is valid in this position"""
        # Row check
        if num in self.grid[row]:
            return False
        # Column check
        if num in [self.grid[r][col] for r in range(9)]:
            return False
        # 3x3 subgrid check
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if self.grid[r][c] == num:
                    return False
        return True

    def is_complete(self):
        return all(all(cell != 0 for cell in row) for row in self.grid)
