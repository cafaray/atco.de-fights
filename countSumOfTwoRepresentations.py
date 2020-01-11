def countSumOfTwoRepresentations(n, l, r):
#    if l+r>n: return 0
#    c=0    
#    while l<=r:
#        if l+r==n:
#            c+=1
#        r-=1
#        l+=1
#    return c
#    return min([(n//2-l), (r-(n//2))]) + (n%2==0) if (n//2) >= l and (n//2)<=r else 1-(n%2==0)
    if (n//2) >= l and (n//2)<=r:
        return min([(n//2-l),(r-(n//2))]) + (n%2==0) + (n%2)
    else:
        return 0
    return sum(1 for a in range(l, r+1) if l <= a <= n - a <= r)
