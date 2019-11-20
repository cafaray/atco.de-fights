def magicalWell(a, b, n):
    m = 0
    for i in range(1,n+1):
        m = m + a * b
        a = a+1
        b = b+1
    return m

N=eval(dir()[0])
m,s=1,0
while m<=N[2]:
    s+=N[0]*N[1]
    N[0]+=1
    N[1]+=1
    m+=1
return s