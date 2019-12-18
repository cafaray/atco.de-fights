def halvingSum(n):
    d,s,i=n,0,1
    while d>0:
        s+=d
        d=n//(2**i)
        i+=1
    return s