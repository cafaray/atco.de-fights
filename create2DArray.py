def create2DArray(lengths):
    r=[]
    for x in lengths:
        z=[i for i in range(x)]
        r.append(z)
    return r