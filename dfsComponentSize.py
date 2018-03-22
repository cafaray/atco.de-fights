def dfsComponentSize(matrix, vertex):
    suma = 0
    for n in range(len(matrix[0])):
        suma += 1 if matrix[vertex][n] else 0
    return suma+1