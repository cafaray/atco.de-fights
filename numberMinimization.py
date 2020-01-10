from itertools import permutations 
def numberMinimization(n, d):
    s=str(n)
    permList = list(permutations(s))
    m=n
    i=0
    while True:        
        perm = permList[i]
        nn=int(''.join(perm))
        p=False
        while nn%d==0:
#            print('\t\tdivide: ', nn,'/',d, nn//d)
            nn = nn//d
            p=True
        if p:
            x=1
            newPerms = sorted(list(permutations(str(nn))))
            for p in newPerms: 
                if p not in permList:
                    permList.insert(i+x,p)
                    x+=1            
        if nn<m:
            #print('\tresult=',m)
            m=nn
        if m<d: return m
        i+=1
        if i>= len(permList): break
    return m

n=2700
d=12
e=1
print("Assertion for extra-test is: ", e==numberMinimization(n, d))

n= 501
d= 3
e= 5
print("Assertion for test 1 is: ", e==numberMinimization(n, d))

n= 4006
d= 2
e= 1
print("Assertion for test 2 is: ", e==numberMinimization(n, d))

n= 321
d= 5
e= 123
print("Assertion for test 3 is: ", e==numberMinimization(n, d))

n= 8381
d= 4
e= 347
print("Assertion for test 4 is: ", e==numberMinimization(n, d))

n= 10477
d= 4
e= 1
print("Assertion for test 5 is: ", e==numberMinimization(n, d))


n= 12722
d= 8
e= 13
print("Assertion for test 6 is: ", e==numberMinimization(n, d))

n= 15456
d= 4
e= 3
print("Assertion for test 7 is: ", e==numberMinimization(n, d))

n= 14840
d= 29
e= 1
print("Assertion for test 8 is: ", e==numberMinimization(n, d))

n= 39979
d= 9
e = 37999
print("Assertion for test 9 is: ", e==numberMinimization(n, d))