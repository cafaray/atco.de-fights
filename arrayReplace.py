def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return list(map(lambda x: substitutionElem if x == elemToReplace else x, inputArray))
