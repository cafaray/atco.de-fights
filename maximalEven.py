def maximalEven(inputArray):
    inputArray = sorted(inputArray)[::-1]
    for x in inputArray:
        if x%2==0:
            return x