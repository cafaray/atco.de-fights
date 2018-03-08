def countInversionsNaive(inputArray):
    increase = 0
    for i in range(len(inputArray)):
        for j in range(len(inputArray)-1,0,-1):
            if inputArray[i] > inputArray[j] and i < j:
                increase = increase + 1
    return increase