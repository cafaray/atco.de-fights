def sortByLength(inputArray):

    s = sorted([len(inputArray[x]) for x in range(len(inputArray))])

    for i in range(len(inputArray)):
        minIndex = i
        tmp = inputArray[i]
        for j in range(i + 1, len(inputArray)):
            if len(inputArray[j]) < len(inputArray[minIndex]):
                minIndex = j
                
        inputArray[i] = inputArray[minIndex]
        inputArray[minIndex] = tmp
    print(inputArray)
    return inputArray



print("Assertion: ", sortByLength(["thitl", "", "sadhxirg", "hx", "ondyxds", "kncor", "sqrg", "hqtchyxku", "rl", "wd"]) == ["", "hx", "rl", "wd", "sqrg", "thitl", "kncor", "ondyxds", "sadhxirg", "hqtchyxku"])