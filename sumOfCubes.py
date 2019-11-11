def sumOfCubes(n):
    return sum([x**3 for x in range(1,n+1)])

def sumOfCubes_V0(n):
    r,x=0,1
    while x<=n:
        r+=x**3
        x+=1
    return r

print(sumOfCubes(3))