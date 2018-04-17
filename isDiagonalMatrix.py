def isDiagonalMatrix(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if x!=y and matrix[x][y]!=0:
                return False
    return True