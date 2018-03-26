def improperFractionToMixed(a):
    ent = a[0]//a[1]
    res = a[0] % a[1]
    return [ent, res, a[1]]