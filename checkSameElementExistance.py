def checkSameElementExistence(arr1, arr2):

    i = 0
    j = 0
    while i<len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            return True
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return False