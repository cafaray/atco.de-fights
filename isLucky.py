def isLucky(n):
    sn = str(n)
    s = len(sn)//2
    f1 = sn[:s]
    f2 = sn[s:]
    n1, n2=0,0
    for x in range(len(f1)):
        n1 += int(f1[x])
        n2 += int(f2[x])
    return n1==n2