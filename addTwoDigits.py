def addTwoDigits(n):
    strNumber = str(n)
    return sum([int(x) for x in strNumber] + [0])