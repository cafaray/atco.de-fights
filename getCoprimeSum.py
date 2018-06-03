def getCoprimeSum(n):    
    if n<2: return n    
    m,N=n,1
    for x in range(2,m+1):        
        p=True
        for y in range(2,int(math.log(x,2))+1):
            if x%y==0:
                p=False
                break
        if p:
            f=False
            while m>1:
                if m%x==0:                    
                    m=m//x
                    f=True                                                
                else:
                    break
            if f:
                N*=(1-(1/x))
            if m==1:break        
    N=(N*n**2)//2
    return int(N)%(10**9+7)