def rightmostRoundNumber(inputArray):
    for x in range(len(inputArray)-1, -1, -1):
        if inputArray[x]%10==0:
            return x
    return -1