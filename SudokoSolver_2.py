# Sudoku Solver

class cell:

    def __init__( self, row, col ):
        self.row = row
        self.col = col
        self.FinalValue = 0
        self.rowStart = 3*(row // 3)
        self.rowEnd = self.rowStart + 2
        self.colStart = 3*(col // 3)
        self.colEnd = self.colStart + 2
        self.impossible = []
        self.possible = []

    def determineImpossible( self, gridVals ):
        for i in range( 0, 9 ):
            if (i != self.col):
                val = gridVals[self.row][i]
                if ( (val != 0) and not(val in self.impossible) ):
                    self.impossible.append( val )

        for i in range( 0, 9 ):
            if (i != self.row):
                val = gridVals[i][self.col]
                if ( (val != 0) and not(val in self.impossible) ):
                    self.impossible.append( val )

        for k in range( self.rowStart, self.rowEnd+1 ):
            for i in range( self.colStart, self.colEnd+1 ):
                if (i != self.col) and (k != self.row):
                    val = gridVals[k][i]
                    if ( (val != 0) and not(val in self.impossible) ):
                        self.impossible.append( val )

        if ( len(self.impossible) == 8 ):
            for i in range( 1, 10 ):
                if not(i in self.impossible):
                    self.FinalValue = i

    def determinePossible( self, gridCells ):
        for j in range( 1, 10 ):
            if not(j in self.impossible):

                excludedFromOthers = True
                for i in range( 0, 9 ):
                    if (i != self.col) and (gridCells[self.row][i].FinalValue == 0):
                        excludedFromOthers = excludedFromOthers and (j in gridCells[self.row][i].impossible)
                if excludedFromOthers:
                    print("test1")
                    self.FinalValue = j

                excludedFromOthers = True
                for i in range( 0, 9 ):
                    if (i != self.row) and (gridCells[i][self.col].FinalValue == 0):
                        excludedFromOthers = excludedFromOthers and (j in gridCells[i][self.col].impossible)
                if excludedFromOthers:
                    print("test2")
                    self.FinalValue = j

                excludedFromOthers = True
                for k in range( self.rowStart, self.rowEnd+1 ):
                    for i in range( self.colStart, self.colEnd+1 ):
                        if (i != self.col) and (k != self.row) and (gridCells[k][i].FinalValue == 0):
                            excludedFromOthers = excludedFromOthers and (j in gridCells[k][i].impossible)
                if excludedFromOthers:
                    print("test3, ",self.row,", ",self.col)
                    self.FinalValue = j

def main():
    gridVals  = [ [ 0 for j in range( 0, 9 ) ] for i in range( 0, 9 ) ]
    gridCells = [ [ cell( i, j ) for j in range( 0, 9 ) ] for i in range( 0, 9 ) ]

    #gridVals[0][1] = 4; gridVals[0][3] = 3; gridVals[0][4] = 5; gridVals[0][5] = 8;
    #gridVals[1][0] = 8; gridVals[1][3] = 4; gridVals[1][4] = 7; gridVals[1][7] = 5;
    #gridVals[2][0] = 5; gridVals[2][2] = 1; gridVals[2][4] = 6; gridVals[2][6] = 8; gridVals[2][8] = 7;
    #gridVals[3][2] = 3; gridVals[3][3] = 6; gridVals[3][4] = 1; gridVals[3][6] = 2;
    #gridVals[4][0] = 2; gridVals[4][8] = 6;
    #gridVals[5][2] = 8; gridVals[5][4] = 3; gridVals[5][5] = 2; gridVals[5][6] = 5;
    #gridVals[6][0] = 3; gridVals[6][2] = 2; gridVals[6][4] = 8; gridVals[6][6] = 7; gridVals[6][8] = 4;
    #gridVals[7][1] = 8; gridVals[7][4] = 4; gridVals[7][5] = 7; gridVals[7][8] = 3;
    #gridVals[8][3] = 9; gridVals[8][4] = 2; gridVals[8][5] = 3; gridVals[8][7] = 8;

    gridVals[0][8] = 8;
    gridVals[1][0] = 6; gridVals[1][3] = 9; gridVals[1][5] = 3; gridVals[1][6] = 4;
    gridVals[2][5] = 7; gridVals[2][7] = 9; gridVals[2][8] = 1;
    gridVals[3][1] = 4; gridVals[3][7] = 2; gridVals[3][8] = 5;
    gridVals[4][1] = 5; gridVals[4][3] = 8; gridVals[4][4] = 4; gridVals[4][5] = 6; gridVals[4][7] = 3;
    gridVals[5][0] = 9; gridVals[5][1] = 6; gridVals[5][7] = 1;
    gridVals[6][0] = 2; gridVals[6][1] = 8; gridVals[6][3] = 7;
    gridVals[7][2] = 6; gridVals[7][3] = 2; gridVals[7][5] = 4; gridVals[7][8] = 9;
    gridVals[8][0] = 7;

    for i in range( 0, 9 ):
        for j in range( 0, 9 ):
            print(gridVals[i][j], end = '  ')
        print()

    print()

    changes = True
    for k in range( 0, 100 ):
        numZeros = 0
        for i in range( 0, 9 ):
            for j in range( 0, 9 ):
                if gridVals[i][j] == 0:
                    numZeros = numZeros + 1
                    gridCells[i][j].determineImpossible( gridVals )
                    gridCells[i][j].determinePossible( gridCells )
                    gridVals[i][j] = gridCells[i][j].FinalValue

        for i in range( 0, 9 ):
            for j in range( 0, 9 ):
                print(gridVals[i][j], end = '  ')
            print()

        input()

        if (numZeros == 0):
            print("Completed in: ",k," iterations")
            print()
            break

        if (k == 24) and (numZeros != 0):
            print()
            print("Puzzle not solved.")
            print()

    for i in range( 0, 9 ):
        for j in range( 0, 9 ):
            print(gridVals[i][j], end = '  ')
        print()

if __name__ == "__main__":
    main()
