def allLongestStrings(inputArray):
    maxlen = max([len(x) for x in inputArray])
    return [elem for elem in inputArray if len(elem)==maxlen]