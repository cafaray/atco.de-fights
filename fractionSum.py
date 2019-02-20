def fractionSum(a, b):
    def gcd(a,b):
        if(a==0):
            return b
        return gcd(b%a,a)
    def lowest(n,d):
        cf = gcd(n,d)
        d=int(d/cf)
        n=int(n/cf)
        return [n,d]
    
    d=gcd(a[1],b[1])
    d=(a[1]*b[1])/d
    n=(a[0]*(d/a[1])+b[0]*(d/b[1]))
    return lowest(n,d)