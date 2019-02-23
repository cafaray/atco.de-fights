def countNeighbouringPairs(inputString):    
    return sum([1 if inputString[x] == inputString[x+1] else 0 for x in range(len(inputString)-1)], 0)
