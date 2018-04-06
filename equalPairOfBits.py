def equalPairOfBits(n, m):
    bn = bin(n)[::-1]
    bm = bin(m)[::-1]
    pos = 0
    for x in range(len(bn)):
        if len(bm) > x:
            print(pos, bn[x], bm[x])
            if bn[x] == bm[x]:
                return math.pow(2, pos)
        pos += 1            
    return -1