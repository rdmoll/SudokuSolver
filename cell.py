import numpy as np

class Cell:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.possible_values = np.arange(1,10)
        self.possible_in_row = np.arange(1,10)
        self.possible_in_col = np.arange(1,10)
        self.possible_in_tile = np.arange(1,10)
        self.tileRow = row // 3
        self.tileCol = col // 3

    def printRowCol(self):
        print(self.row, " , ", self.col, " , ", self.value)

    def update_possible(self, val_grid):
        for i in range(0, 9):
            if (i != self.col):
                self.possible_values = np.delete(self.possible_values, np.argwhere(self.possible_values == val_grid[self.row][i]))

        for i in range(0, 9):
            if (i != self.row):
                self.possible_values = np.delete(self.possible_values, np.argwhere(self.possible_values == val_grid[i][self.col]))

        for i in range(3*self.tileRow, 3*self.tileRow + 3):
            for j in range(3*self.tileCol, 3*self.tileCol + 3):
                if (i != self.col and j != self.row):
                    self.possible_values = np.delete(self.possible_values, np.argwhere(self.possible_values == val_grid[i][j]))

        if (self.possible_values.size == 1):
            self.value = self.possible_values[0]

    def update_unique(self, cell_grid):
        for pv in self.possible_values:

            rowUnique = True
            for i in range(0, 9):
                if (i != self.col):
                    if pv in cell_grid[self.row][i].possible_values:
                        rowUnique = False

            colUnique = True
            for i in range(0, 9):
                if (i != self.row):
                    if pv in cell_grid[i][self.col].possible_values:
                        colUnique = False

            squareUnique = True
            for i in range(3*self.tileRow, 3*self.tileRow + 3):
                for j in range(3*self.tileCol, 3*self.tileCol + 3):
                    #print(self.tileRow," , ",self.tileCol)
                    if (i != self.col and j != self.row):
                        if pv in cell_grid[i][j].possible_values:
                            squareUnique = False

            if (rowUnique or colUnique or squareUnique):
                self.value = pv
                self.possible_values = [pv]
                break
