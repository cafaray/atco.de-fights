def prefixSums(a):
    r=[]
    for i in range(len(a)):
        r+=[sum([x for x in a[:i+1]])]
    return r