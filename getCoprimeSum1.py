def getCoprimeSum(n):
    def coPrime(x):
        y=n
        while y>=1:
            x,y=y,x%y            
        return x       
    v=0
    #p=(n%2==0)
    d = dict()
    for x in range(1,n+1):
    #    if p and x%2==0:
    #        continue        
        cp = coPrime(x);
        d[x]=cp
        if cp==1: v+=x        
    for k,r in d.items():
        print(k, r)
    return v%1000000007


n=10
print(getCoprimeSum(n))