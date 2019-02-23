def isSkewSymmetricMatrix(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y]==matrix[y][x]*-1:
                continue
            else:
                return False    
    return True