def divideAsLongAsPossible(n, d):
    cnt = 1
    nn = n
    for x in range(n):
        if nn % d != 0:            
            break
        nn /= d
    return nn