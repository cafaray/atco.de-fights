def equationSolutions(l, r):
    pairs=[]
    for x in range(l, r+1):
        if x >= l and x <= r:
            for y in range(l, r+1):
                if x >= l and x <= r:
                    if x**3 == y**2:
                        pairs += [(x,y)]
    return len(pairs)
