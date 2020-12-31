# SudokuSolver
import numpy as np
import pandas as pd
from cell import *
from divData import *

# Function for printing grid
def print_grid(val_grid):
    for i in range( 0, 9 ):
        for j in range( 0, 9 ):
            print(val_grid[i][j], end = '  ')
        print()
    print()

def main():

    # Read initial grid from csv file
    val_grid_trans = pd.read_csv("inputGridExpert.csv",header=None)
    val_grid = np.transpose(val_grid_trans)

    # Initialize grid cells, rows, cols, and tiles
    cell_grid = [ [ Cell(i, j, val_grid[i][j]) for j in range(0, 9) ] for i in range(0, 9) ]
    rows = [ RowData(i) for i in range(0, 9) ]
    cols = [ ColData(i) for i in range(0, 9) ]
    tiles = [ [ TileData(i, j) for j in range(0, 3) ] for i in range(0, 3) ]

    # Print initial grid
    print_grid(val_grid)
    print()

    # Loop through checks
    for t in range(0,10):

        # Find grid cells with only 1 possible values
        for i in range(0, 9):
            for j in range(0, 9):
                if (cell_grid[i][j].value == 0):
                    cell_grid[i][j].update_possible(val_grid)

        # Find missing values in rows, cols, and tiles which are only
        # possible for one cell
        for i in range(0, 9):
            rows[i].update_missing(cell_grid)
            cols[i].update_missing(cell_grid)
        for i in range(0, 3):
            for j in range(0, 3):
                tiles[i][j].update_missing(cell_grid)

        # Update val_grid
        for i in range(0, 9):
            for j in range(0, 9):
                val_grid[i][j] = cell_grid[i][j].value

    # Print result grid, run accuracy checks
    print_grid(val_grid)
    print()
    for i in range(0, 9):
        rows[i].check_complete(cell_grid)
    for i in range(0, 9):
        cols[i].check_complete(cell_grid)
    for i in range(0, 3):
        for j in range(0, 3):
            tiles[i][j].check_complete(cell_grid)

if __name__ == "__main__":
    main()
