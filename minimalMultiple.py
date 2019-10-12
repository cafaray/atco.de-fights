def minimalMultiple(divisor, lowerBound):
    while lowerBound%divisor!=0: lowerBound+=1
    return lowerBound