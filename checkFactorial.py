def checkFactorial(n):
    f=1
    x=2
    while f<n:
        f*=x
        x+=1
    return f==n