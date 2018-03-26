def isSkewSymmetricMatrix(m):
    for x in range(len(m)):
        for y in range(len(m)):
            if m[x][y]!=-m[y][x]: return 0 
    return 1 