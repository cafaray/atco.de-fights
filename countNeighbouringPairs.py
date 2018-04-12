def countNeighbouringPairs(inputString):
    c = 0
    for x in range(len(inputString)-1):
        if inputString[x] == inputString[x+1]:
            c += 1
    return c