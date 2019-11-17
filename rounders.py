def rounders(n):
    c=1
    f0=(10**c)
    while n//f0>0:                
        f1=(10**(c-1))
        i=n%f0//f1
        if i>=5:
            n+=(f0)
        n-=i*(f1)
        c+=1  
        f0=(10**c)              
    return n

def rounders_vs(value):
    svalue = str(value)[::-1]
    for s in range(0,len(svalue)-1):
        #print(s, '=', int(svalue[s]))
        #print(s, svalue, svalue[s])
        if int(svalue[s])>=5: 
            nval = int(svalue[s])*(10**s)            
            value = value - nval + (10**(s+1))
            #print('-> ',s, nval, value)
        else:
            nval = int(svalue[s])*(10**s)     
            #print('nval =', int(svalue[s]), '*', (10**s), ' =', nval)
            value = value - (int(svalue[s]) *  (10**s))
            #print('<- ',s, nval, value)
        svalue = str(value)[::-1]
        #print('nuevo:',svalue)
    return value

n=15
e=20
r=rounders(n)
print('Assertion ', e, "==", r, ": ", e==r)

n=1234
e=1000
r=rounders(n)
print('Assertion ', e, "==", r, ": ", e==r)

n=1445
e=2000
r=rounders(n)
print('Assertion ', e, "==", r, ": ", e==r)

n=10
e=10
r=rounders(n)
print('Assertion ', e, "==", r, ": ", e==r)

n=7001
e=7000
r=rounders(n)
print('Assertion ', e, "==", r, ": ", e==r)

n=99
e=100
r=rounders(n)
print('Assertion ', e, "==", r, ": ", e==r)