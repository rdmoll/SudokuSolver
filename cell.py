import numpy as np

class Cell:

    def __init __(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.possible = np.arange(1,10)

    def update(self, grid):
        
