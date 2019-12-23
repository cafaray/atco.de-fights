def divisorsSubset(subset, n):    
    ss=sorted(subset)
    i=ss[0]
    c=0
    while i<=n:
        inside=True
        for x in ss[::-1]:
            if i%x!=0:
                inside=False
                break
        if inside:
            c+=1
        i+=1
    return c 


def divisorsSubset_old(subset, n):    
    c=0
    for i in range(1,n+1):
        l=True
        for j in subset:
            if i%j!=0:
                l=False
        if l: c+=1
    return c