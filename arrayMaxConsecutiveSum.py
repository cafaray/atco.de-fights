def arrayMaxConsecutiveSum(inputArray, k):
    
    return max([sum(inputArray[x: x+k]) for x in range(0, len(inputArray))])