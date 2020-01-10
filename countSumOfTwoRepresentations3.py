def countSumOfTwoRepresentations3(n, l, r):
    c=0
    while r>=l:
        if l<=(n-r)<=r:
            c+=1        
        elif (n-r)>r:
            break
        r-=1
    return c

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