# Sudoku Solver

class cell:
    impossible = []
    possible = range( 0, 9 )

    def __init__( self, row, col ):
        self.row = row
        self.col = col
        self.FinalValue = 0
        self.rowStart = row // 3
        self.rowEnd = self.rowStart + 2
        self.colStart = col // 3
        self.colEnd = self.colStart + 2

    def determineCellValue( self ):
        if ( len(self.impossible) == 8 ):
            for i in range( 1, 10 ):
                if not(i in self.impossible):
                    self.FinalValue = i

    def determineImpossible( self, gridVals ):
        for i in range( 0, 9 ):
            if ( i != self.col ):
                val = gridVals[self.row][i]
                if not( val in self.impossible ) and ( val != 0 ):
                    self.impossible.append( val )
            if ( i != self.row ):
                val = gridVals[i][self.col]
                if not( val in self.impossible ) and ( val != 0 ):
                    self.impossible.append( val )
        for i in range( self.rowStart, self.rowEnd ):
            for j in range( self.colStart, self.colEnd ):
                if ( j != self.col ) and ( i != self.row ):
                    val = gridVals[j][i]
                    if not( val in self.impossible ) and ( val != 0 ):
                        self.impossible.append( val )

def main():
    gridVals  = [ [ 0 for j in range( 0, 9 ) ] for i in range( 0, 9 ) ]
    gridCells = [ [ cell( j, i ) for j in range( 0, 9 ) ] for i in range( 0, 9 ) ]

    gridVals[0][1] = 4; gridVals[0][3] = 3; gridVals[0][4] = 5; gridVals[0][5] = 8;
    gridVals[1][0] = 8; gridVals[1][3] = 4; gridVals[1][4] = 7; gridVals[1][7] = 5;
    gridVals[2][0] = 5; gridVals[2][2] = 1; gridVals[2][4] = 6; gridVals[2][6] = 8; gridVals[2][8] = 7;
    gridVals[3][2] = 3; gridVals[3][3] = 6; gridVals[3][4] = 1; gridVals[3][6] = 2;
    gridVals[4][0] = 2; gridVals[4][8] = 6;
    gridVals[5][2] = 8; gridVals[5][4] = 3; gridVals[5][5] = 2; gridVals[5][6] = 5;
    gridVals[6][0] = 3; gridVals[6][2] = 2; gridVals[6][4] = 8; gridVals[6][6] = 7; gridVals[6][8] = 4;
    gridVals[7][1] = 8; gridVals[7][4] = 4; gridVals[7][5] = 7; gridVals[7][8] = 3;
    gridVals[8][3] = 9; gridVals[8][4] = 2; gridVals[8][5] = 3; gridVals[8][7] = 8;

    #for i in range( 0, 9 ):
    #    for j in range( 0, 9 ):
    #        if ( gridCells[j][i].FinalValue == 0 ):
    #            gridCells[j][i].determineImpossible( gridVals )
    #            gridCells[j][i].determineCellValue()
    #            gridVals[j][i] = gridCells[j][i].FinalValue

    for i in range( 0, 9 ):
        for j in range( 0, 9 ):
            print(gridVals[i][j], end = '  ')
        print()

if __name__ == "__main__":
    main()
