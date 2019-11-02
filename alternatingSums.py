def alternatingSums(a):
    return [sum([a[x] for x in range(len(a)) if x%2==0])] + [sum([a[x] for x in range(len(a)) if x%2!=0])]

def alternatingSums_V1(a):
    r=[0,0]
    i,z=0,len(a)
    while True:
        if i<z:r[0]+=a[i]        
        if i+1<z:r[1]+=a[i+1]
        if i>=z:break
        i+=2
    return r