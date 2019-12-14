def maxDigit(n):
    md=0
    while n>0:
        if md<n%10:
            md=n%10
        n/=10
    return md