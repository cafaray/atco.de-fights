def isSum(value):
    s = 0
    for x in range(0,value+1):
        s += x
        if s == value:
            return True
        elif s > value:
            return False
    return False