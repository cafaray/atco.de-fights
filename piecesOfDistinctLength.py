def piecesOfDistinctLengths(strawLength):
    n = math.sqrt(2*strawLength)
    if n*(n+1)/2 > strawLength: return n-1
    return n