def factorialTrailingZeros(n):    
    def factorialString(n):
        f=1
        for i in range(1,n+1):
            f*=i
        return str(f)
    
    f,r= factorialString(n)[::-1],0
    for c in f:
        if c!='0':
            break
        r+=1
    return r