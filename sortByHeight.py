def sortByHeight(a):
    sor = sorted([x for x in a if x >=0])
    y = 0
    for x in range(len(a)):
        if a[x] >= 0:
            a[x] = sor[y]
            y+=1
    return a
