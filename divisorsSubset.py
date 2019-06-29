def divisorsSubset(subset, n):    
    c=0
    for i in range(1,n+1):
        l=True
        for j in subset:
            if i%j!=0:
                l=False
        if l: c+=1
    return c