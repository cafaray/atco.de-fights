def piecesOfDistinctLengths(strawLength):
    n=math.sqrt(2*strawLength)
    n=round(n)
    if n*(n+1)/2>strawLength: 
        return n-1
    else:
        return n
