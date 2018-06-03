def getCoprimeSum(n):    
    if n < 2: return n
    
    def phi(n):
        N = 1
        for x in range(2, n + 1):        
            prime=True
            for y in range(2, int(x**0.5) + 1):
                if x%y==0:
                    prime = False
                    break
            if prime:
                factor=False
                while n>1:
                    if n%x==0:                    
                        n=n//x
                        factor=True                                                
                    else:
                        break
                if factor:
                    N*=(1-(1/x))
                if n==1: break
        return N
    N=(phi(n)*n**2)//2
    return int(N)%1000000007
    