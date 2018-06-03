def primes(n):
    noprimes = set(j for i in range(2, n) for j in range(i*2, n, i))
    prime = [x for x in range(1,n+1) if x not in noprimes]
    return prime

print(primes(50))

def getCoprimeSum(n):    
    s,x=0,0        
    while x<=n:
        y,z=n,x        
        while y>0:
            z,y=y,z%y
            if z==1:
                s+=x
                break        
        x+=1
    return s%1000000007