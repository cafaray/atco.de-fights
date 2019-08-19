def fibonacciNumber(n):
    if n==0: return 0
    if n==1: return 1
    if n==2: return 1
    x,y = 0,1
    i=2
    while i<=n:
        z=x+y
        x,y=y,z        
        i+=1
    return z