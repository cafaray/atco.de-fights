def differentValues(a, d):
    res = -1
    for x in range(len(a)):
        for y in range(x+1,len(a)):
            if res < abs(a[x] - a[y]) <= d:
                res = abs(a[x] - a[y])
    return res