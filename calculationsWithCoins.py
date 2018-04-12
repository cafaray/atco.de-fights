def calculationsWithCoins(a, b, c):
    x = a + b
    y = a + c
    z = b + c
    w = a + b + c
    s = set([a, b, c, x, y, z, w])
    return len(list(s))