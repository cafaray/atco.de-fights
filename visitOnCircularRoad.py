def visitsOnCircularRoad(n, visitsOrder):
    m=n//2
    if visitsOrder[0]==1:
        s=0     
    else: 
        s = abs(visitsOrder[0]-1)
        if s>m:
            s=abs(n-visitsOrder[0]+1)
    for i in range(1,len(visitsOrder)):
        d=abs(visitsOrder[i-1]-visitsOrder[i])
        if d>m: 
            d=abs(n-visitsOrder[i-1]+1)
        s+=d 
    return s


n=5
visitsOrder=[3,2]
r=3
# print("Assertion at sample 1:", visitsOnCircularRoad(n, visitsOrder)==r)

n=6
visitsOrder=[3,3,2,5,6,1]
r=8
# print("Assertion at sample 2:", visitsOnCircularRoad(n, visitsOrder)==r)

n=6
visitsOrder=[5]
r=2
# print("Assertion at sample 3:", visitsOnCircularRoad(n, visitsOrder)==r)

n=5
visitsOrder=[2,3,5,4,1]
r=7
# print("Assertion at sample 4:", visitsOnCircularRoad(n, visitsOrder)==r)


n=4
visitsOrder=[1, 3, 2, 3, 1]
r=6
# print("Assertion at Test 1:", visitsOnCircularRoad(n, visitsOrder)==r)

n=3
visitsOrder=[3]
r=1
# print("Assertion at Test 1:", visitsOnCircularRoad(n, visitsOrder)==r)

n=5
visitsOrder=[2,5,2,1,4]
r=8
print("Assertion at Test 1:", visitsOnCircularRoad(n, visitsOrder)==r)