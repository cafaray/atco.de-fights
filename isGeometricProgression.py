def isGeometricProgression(sequence):
    #sequence = sorted(sequence)
    f = sequence[1]/sequence[0]
    for x in range(1,len(sequence)-1):
        if sequence[x+1] / sequence[x]!=f:
            return False
    return True