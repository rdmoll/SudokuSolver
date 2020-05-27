# Sudoku Solver

from cell import *

def print_grid(val_grid):
    for i in range( 0, 9 ):
        for j in range( 0, 9 ):
            print(val_grid[i][j], end = '  ')
        print()
    print()

def main():
    val_grid = [ [ 0 for j in range( 0, 9 ) ] for i in range( 0, 9 ) ]

    #val_grid[0][1] = 4; val_grid[0][3] = 3; val_grid[0][4] = 5; val_grid[0][5] = 8;
    #val_grid[1][0] = 8; val_grid[1][3] = 4; val_grid[1][4] = 7; val_grid[1][7] = 5;
    #val_grid[2][0] = 5; val_grid[2][2] = 1; val_grid[2][4] = 6; val_grid[2][6] = 8; val_grid[2][8] = 7;
    #val_grid[3][2] = 3; val_grid[3][3] = 6; val_grid[3][4] = 1; val_grid[3][6] = 2;
    #val_grid[4][0] = 2; val_grid[4][8] = 6;
    #val_grid[5][2] = 8; val_grid[5][4] = 3; val_grid[5][5] = 2; val_grid[5][6] = 5;
    #val_grid[6][0] = 3; val_grid[6][2] = 2; val_grid[6][4] = 8; val_grid[6][6] = 7; val_grid[6][8] = 4;
    #val_grid[7][1] = 8; val_grid[7][4] = 4; val_grid[7][5] = 7; val_grid[7][8] = 3;
    #val_grid[8][3] = 9; val_grid[8][4] = 2; val_grid[8][5] = 3; val_grid[8][7] = 8;

    val_grid[0][8] = 8;
    val_grid[1][0] = 6; val_grid[1][3] = 9; val_grid[1][5] = 3; val_grid[1][6] = 4;
    val_grid[2][5] = 7; val_grid[2][7] = 9; val_grid[2][8] = 1;
    val_grid[3][1] = 4; val_grid[3][7] = 2; val_grid[3][8] = 5;
    val_grid[4][1] = 5; val_grid[4][3] = 8; val_grid[4][4] = 4; val_grid[4][5] = 6; val_grid[4][7] = 3;
    val_grid[5][0] = 9; val_grid[5][1] = 6; val_grid[5][7] = 1;
    val_grid[6][0] = 2; val_grid[6][1] = 8; val_grid[6][3] = 7;
    val_grid[7][2] = 6; val_grid[7][3] = 2; val_grid[7][5] = 4; val_grid[7][8] = 9;
    val_grid[8][0] = 7;

    print_grid(val_grid)

    cell_grid = [ [ Cell(i, j, val_grid[i][j]) for j in range(0, 9) ] for i in range(0, 9) ]

    for k in range(0, 5):
        for i in range(0, 9):
            for j in range(0, 9):
                if (cell_grid[i][j].value == 0):
                    cell_grid[i][j].update_possible(val_grid)
                    cell_grid[i][j].update_unique(cell_grid)
                    if (cell_grid[i][j] != 0):
                        val_grid[i][j] = cell_grid[i][j].value

        #print_grid(val_grid)

if __name__ == "__main__":
    main()
