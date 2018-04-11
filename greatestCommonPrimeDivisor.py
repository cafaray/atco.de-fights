def greatestCommonPrimeDivisor(a, b):
    j=-1
    for i in range(2,min(a,b)+1):
        if a%i==b%i==0:
            j=i
        while a%i==0:
            a//=i
        while b%i==0:
            b//=i
    return j