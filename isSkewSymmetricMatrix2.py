def isSkewSymmetricMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != -1*matrix[j][i]:
                return False
    return True