def adjacentElementsProduct(inputArray):
    #return max([inputArray[x]*inputArray[x-1] for x in range(1,len(inputArray))])
    return max(list(map(lambda x, y: x*y, inputArray[0:len(inputArray)-1], inputArray[1:len(inputArray)])))