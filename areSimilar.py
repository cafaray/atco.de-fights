def areSimilar(a, b):
    k=0
    c= a[:]
    d= b[:]
    c.sort()
    d.sort()
    #print(c, d)
    if c!= d:
        return False
    for i in range(len(a)):
        if a[i]!= b[i]:
            k+=1
    if k== 0 or k==2:
        return True
    return False