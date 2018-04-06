def sortByLength(inputArray):

    for i in range(len(inputArray)):
        minIndex = i
        tmp = inputArray[i]
        for j in range(i + 1, len(inputArray)):
            if len(inputArray[j]) < len(inputArray[minIndex]):
                minIndex = j
        inputArray[i] = inputArray[minIndex]
        inputArray[minIndex] = tmp

    return inputArray