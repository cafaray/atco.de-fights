def lsb(n):
    b = bin(n)
    #print(b)
    r=0
    for c in range(len(b)-1,1,-1):
        #print(b[c])
        if int(b[c]) & 1:
            return r
        r+=1
    return -1

def continuedFraction(fraction):
    res=[]
    ni = fraction[0]
    i = fraction[0]//fraction[1] 
    res+=[i]   
    while ni !=0:
        
        print("i=", i)
        r = i*fraction[1]
        ni = fraction[0]-r
        reverseFraction = [fraction[1],ni]
        fraction = reverseFraction    
    if len(res)%2==0:
        number = res[-1] - 1
        res[1]=number
        res+=[1]
    b = binaryConstructor(res)[::-1]
    bn = sum([(2**x)*int(b[x]) for x in range(0,len(b))],0)
    print(b, bn)
    return bn

def binaryConstructor(fractions):
    b=True
    v=''
    for x in fractions[::-1]:
        for y in range(x):
            if b:
                v+='1'
            else: 
                v+='0'
        b = not b    
    return v

print("Assertion result on [5,2] = ", continuedFraction([5,2])==11)
print("Assertion result on [1,3] = ", continuedFraction([1,3])==3)
print("Assertion result on [14,3] = ", continuedFraction([14,3])==110)
print("Assertion result on [7,13] = ", continuedFraction([7,13])==129)
print("Assertion result on [3,4] = ", continuedFraction([3,4])==13)
print("Assertion result on [4,3] = ", continuedFraction([4,3])==8)
print("Assertion result on [53,37] = ", continuedFraction([53,37])==1080)
print("Assertion result on [37,53] = ", continuedFraction([37,53])==1989)


#print("17=", lsb(17))
#print("2=", lsb(2))
#print("3=", lsb(3))
#print("4=", lsb(4))
#print("1=", lsb(1))

