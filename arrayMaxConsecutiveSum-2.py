def arrayMaxConsecutiveSum(inputArray, k):
    maxn = 0
    for element in range(len(inputArray) - k + 1):
        suma = sum(inputArray[element:element+k])
        if maxn < suma: maxn = suma
    return maxn