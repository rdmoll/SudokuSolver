import numpy as np

class Cell:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.tile_row = row // 3
        self.tile_col = col // 3
        self.value = value
        if value == 0:
            self.possible_values = np.arange(1,10)
        else:
            self.possible_values = np.arange(value,value+1)

    def update_possible(self, val_grid):

        # Scan row
        for i in range(0, 9):
            if (i != self.row):
                self.possible_values = np.delete(self.possible_values, np.argwhere(self.possible_values == val_grid[i][self.col]))

        # Scan column
        for i in range(0, 9):
            if (i != self.col):
                self.possible_values = np.delete(self.possible_values, np.argwhere(self.possible_values == val_grid[self.row][i]))

        # Scan tile
        for i in range(3*self.tile_row, 3*self.tile_row + 3):
            for j in range(3*self.tile_col, 3*self.tile_col + 3):
                if (i != self.col and j != self.row):
                    self.possible_values = np.delete(self.possible_values, np.argwhere(self.possible_values == val_grid[i][j]))

        # If there is only one possible value
        if (self.possible_values.size == 1):
            self.value = self.possible_values[0]
