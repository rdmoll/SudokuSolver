import numpy as np
from tallyMissing import *

class RowData:

    def __init__(self, index):
        self.index = index
        self.values_missing = np.arange(1,10)

    def update_missing(self, cell_grid):
        self.row_array = [cell_grid[self.index][i].value for i in range(0,9)]

        for i in range(0,9):
            self.values_missing = np.delete(self.values_missing, np.argwhere(self.values_missing == self.row_array[i]))

        self.row_tallies = [ RowTallyMissing(self.index, self.values_missing[i], cell_grid) for i in range(0, self.values_missing.size) ]

        for i in range(0, self.values_missing.size):
            if self.row_tallies[i].possible_cells.size == 1:
                cell_grid[self.index][self.row_tallies[i].possible_cells[0]].value = self.values_missing[i]
                cell_grid[self.index][self.row_tallies[i].possible_cells[0]].possible_values = [self.values_missing[i]]

    def check_complete(self, cell_grid):
        self.row_array = [cell_grid[self.index][i].value for i in range(0,9)]

        for i in range(0,9):
            self.values_missing = np.delete(self.values_missing, np.argwhere(self.values_missing == self.row_array[i]))

        if self.values_missing.size == 0:
            print("Row ",self.index+1," complete")
        else:
            print("Row ",self.index+1," incomplete: ",self.values_missing)

class ColData:

    def __init__(self, index):
        self.index = index
        self.values_missing = np.arange(1,10)

    def update_missing(self, cell_grid):
        self.col_array = [cell_grid[i][self.index].value for i in range(0,9)]

        for i in range(0,9):
            self.values_missing = np.delete(self.values_missing, np.argwhere(self.values_missing == self.col_array[i]))

        self.col_tallies = [ ColTallyMissing(self.index, self.values_missing[i], cell_grid) for i in range(0, self.values_missing.size) ]

        for i in range(0, self.values_missing.size):
            if self.col_tallies[i].possible_cells.size == 1:
                cell_grid[self.col_tallies[i].possible_cells[0]][self.index].value = self.values_missing[i]
                cell_grid[self.col_tallies[i].possible_cells[0]][self.index].possible_values = [self.values_missing[i]]

    def check_complete(self, cell_grid):
        self.col_array = [cell_grid[i][self.index].value for i in range(0,9)]

        for i in range(0,9):
            self.values_missing = np.delete(self.values_missing, np.argwhere(self.values_missing == self.col_array[i]))

        if self.values_missing.size == 0:
            print("Col ",self.index+1," complete")
        else:
            print("Col ",self.index+1," incomplete: ",self.values_missing)

class TileData:

    def __init__(self, row_index, col_index):
        self.row_index = row_index
        self.col_index = col_index
        self.values_missing = np.arange(1,10)

    def update_missing(self, cell_grid):
        self.tile_array = [cell_grid[self.row_index * 3 + i][self.col_index * 3 + j].value for i in range(0,3) for j in range(0,3)]

        for i in range(0,9):
            self.values_missing = np.delete(self.values_missing, np.argwhere(self.values_missing == self.tile_array[i]))

        self.col_tallies = [ TileTallyMissing(self.row_index, self.col_index, self.values_missing[i], cell_grid) for i in range(0, self.values_missing.size) ]

        for i in range(0, self.values_missing.size):
            if self.col_tallies[i].possible_cells.shape[0] == 1:
                cell_grid[self.col_tallies[i].possible_cells[0][0]][self.col_tallies[i].possible_cells[0][1]].value = self.values_missing[i]
                cell_grid[self.col_tallies[i].possible_cells[0][0]][self.col_tallies[i].possible_cells[0][1]].possible_values = [self.values_missing[i]]

    def check_complete(self, cell_grid):
        self.tile_array = [cell_grid[self.row_index * 3 + i][self.col_index * 3 + j].value for i in range(0,3) for j in range(0,3)]

        for i in range(0,9):
            self.values_missing = np.delete(self.values_missing, np.argwhere(self.values_missing == self.tile_array[i]))

        if self.values_missing.size == 0:
            print("Tile (",self.row_index+1,",",self.col_index+1,") complete")
        else:
            print("Tile (",self.row_index+1,",",self.col_index+1,") incomplete: ",self.values_missing)
