def differentSubstringsTrie(inputString):
    ss = set()
    for i in range(len(inputString)):
        for j in range(i, len(inputString)):
            ss.add(inputString[i:j+1])
    return len(ss)