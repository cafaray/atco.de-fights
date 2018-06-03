import fractions
def getCoprimeSum(n):
    v=0
    r = [0 for x in range(n+1)]
    for x in range(1,(n+1)//2):
        if fractions.gcd(n, x)==1: 
            r[x]=x 
            r[n-x]=n-x 
    print(r)
    return sum(r)%1000000007

print(getCoprimeSum(237))