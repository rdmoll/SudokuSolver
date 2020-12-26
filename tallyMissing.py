import numpy as np

class RowTallyMissing:

    def __init__(self, index, value, cell_grid):
        self.value = value
        self.possible_cells = np.array([], dtype=int)
        for i in range(0,9):
            if value in cell_grid[index][i].possible_values:
                self.possible_cells = np.append(self.possible_cells,i)

class ColTallyMissing:

    def __init__(self, index, value, cell_grid):
        self.value = value
        self.possible_cells = np.array([], dtype=int)
        for i in range(0,9):
            if value in cell_grid[i][index].possible_values:
                self.possible_cells = np.append(self.possible_cells,i)

class TileTallyMissing:

    def __init__(self, row_index, col_index, value, cell_grid):
        self.value = value
        self.possible_cells = np.empty((0,2), dtype=int)
        for i in range(0,3):
            for j in range(0,3):
                row_idx = row_index * 3 + i
                col_idx = col_index * 3 + j
                if value in cell_grid[row_idx][col_idx].possible_values:
                    self.possible_cells = np.append(self.possible_cells, [[row_idx,col_idx]], axis=0)
