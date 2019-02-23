def inverseMatrix(matrix):
    m=[[matrix[y][x] for y in range(len(matrix[x]))] for x in range(len(matrix))]
    return m


def inverseMatrixReverse(matrix):
    m=[[matrix[y][x]*-1 for y in range(len(matrix[x]))] for x in range(len(matrix))]
    return m
    
matrix = [[ 0, 0,  1], [ 0, 0, -2], [-1, 2,  0]]
print(inverseMatrix(matrix))
