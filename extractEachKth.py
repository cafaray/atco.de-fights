def extractEachKth(inputArray, k):
    array = list()
    count = 0
    for elementK in range(0, len(inputArray)):
        count = count + 1
        if count % k == 0:
            continue
        array.append(inputArray[elementK])
    return array