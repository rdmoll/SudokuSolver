import numpy as np

class Cell:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.possible_values = np.arange(1,10)

    def update_possible(self, val_grid):
        for i in range(0, 9):
            if (i != self.col):
                self.possible_values = np.delete(self.possible_values, np.argwhere(self.possible_values == val_grid[self.row][i]))

        for i in range(0, 9):
            if (i != self.row):
                self.possible_values = np.delete(self.possible_values, np.argwhere(self.possible_values == val_grid[i][self.col]))

        self.possible_values = np.delete(self.possible_values, np.argwhere(self.possible_values == val_grid[self.row + 1][self.col + 1]))
        self.possible_values = np.delete(self.possible_values, np.argwhere(self.possible_values == val_grid[self.row + 1][self.col - 1]))
        self.possible_values = np.delete(self.possible_values, np.argwhere(self.possible_values == val_grid[self.row - 1][self.col + 1]))
        self.possible_values = np.delete(self.possible_values, np.argwhere(self.possible_values == val_grid[self.row - 1][self.col - 1]))

        if (self.possible_values == 1):
            self.value = self.possible_values[0]

    def update_unique(self, cell_grid):
        for pv in self.possible_values:

            unique = True
            for i in range(0, 9):
                if (i != self.col and cell_grid[self.row][i].value == 0):
                    if pv in cell_grid[self.row][i].possible_values:
                        unique = False

            for i in range(0, 9):
                if (i != self.row and cell_grid[i][self.col].value == 0):
                    if pv in cell_grid[i][self.col].possible_values:
                        unique = False

            if (cell_grid[self.row + 1][self.col + 1].value == 0):
                if pv in cell_grid[self.row + 1][self.col + 1].possible_values:
                    unique = False

            if (cell_grid[self.row + 1][self.col - 1].value == 0):
                if pv in cell_grid[self.row + 1][self.col - 1].possible_values:
                    unique = False

            if (cell_grid[self.row - 1][self.col + 1].value == 0):
                if pv in cell_grid[self.row - 1][self.col + 1].possible_values:
                    unique = False

            if (cell_grid[self.row - 1][self.col - 1].value == 0):
                if pv in cell_grid[self.row - 1][self.col - 1].possible_values:
                    unique = False

            if (unique):
                self.value = pv
