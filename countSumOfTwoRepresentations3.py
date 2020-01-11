def countSumOfTwoRepresentations3(n, l, r):
    # first solution with brute force, time exceeded :(
    c=0
    while r>=l:
        if l<=(n-r)<=r:
            c+=1        
        elif (n-r)>r:
            break
        r-=1
    return c

    # a better approach using o(1) solution, nice :)
    if (n//2) >= l and (n//2)<=r:
        return min([(n//2-l),(r-(n//2))]) + (n%2==0) + (n%2)
    else:
        return 0
    return sum(1 for a in range(l, r+1) if l <= a <= n - a <= r)


n=24
l=8
r=16
e=5
f=countSumOfTwoRepresentations3(n,l,r)
print("Assertion for Test 7 is:", f, '==',e,":", f==e)

n=5
l=1
r=5
e=2
f=countSumOfTwoRepresentations3(n,l,r)
print("Assertion for Test 7 is:", f, '==',e,":", f==e)