def sumOfTwo(a, b, v):
    sa = set(a)
    return any(v - x in sa for x in b)