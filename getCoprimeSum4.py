def getCoprimeSum(n):    
    v=0
    n2=(n+1)//2
    for x in range(n2):
        y=n
        while y!=0:
            x,y = y,x%y

        if x==1: v+=n
    return v%1000000007

print(getCoprimeSum(5400))