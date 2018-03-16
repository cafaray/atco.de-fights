def isSum(value):
    s = 1
    c = 2
    while s < value:
        s += c
        c += 1
    return s == value