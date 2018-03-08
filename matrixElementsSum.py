def matrixElementsSum(matrix):
    increase = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):            
            if x>0:
                if matrix[x-1][y] > 0 and matrix[x][y] > 0: 
                    increase+=[matrix[x][y]]
                else:
                    matrix[x][y] = 0
            else:
                if matrix[x][y] > 0:
                    increase+=[matrix[x][y]]
    return sum(increase)