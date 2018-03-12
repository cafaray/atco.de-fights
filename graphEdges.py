def graphEdges(matrix):

    edges = 0

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]:
                edges += 1

    return  edges/2