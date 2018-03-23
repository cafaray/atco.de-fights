def sudoku(grid):
    for k in grid:
        if [1,2,3,4,5,6,7,8,9] != sorted(k):
            #print(sorted(k))
            return False    
    
    for i in range(0,9):
        k = [grid[j][i] for j in range(0, 9)]            
        #print(sorted(k))
        if [1,2,3,4,5,6,7,8,9] != sorted(k):
            return False
    return blockSudoku(grid)


def blockSudoku(grid):
    modulo = []
    bloque = 0
    while bloque < 3:
        squares = []
        for r in range(1, len(grid)+1):            
            t = [str(grid[r-1][g]) for g in range(3*bloque,3*(bloque+1))]
            squares.append(''.join(t))
            if r % 3 == 0 or r == len(grid):
                sudok = ''.join(squares)
                print(sorted(sudok))                
                modulo.append(squares)
                if ['1','2','3','4','5','6','7','8','9'] != sorted(sudok):
                    return False
                squares=[]
        bloque += 1                        
    print(modulo)
    return True