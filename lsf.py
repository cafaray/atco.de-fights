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
        print(ni)
        reverseFraction = [fraction[1],ni]
        print(reverseFraction)
        fraction = reverseFraction    
        i = fraction[0]//fraction[1]
    
    #fraction = reverseFraction
    #i = fraction[0]//fraction[1]
    #print("i=", i)
    #r = i*fraction[1]
    #ni = fraction[0]-r
    #print(ni)
    #reverseFraction = [fraction[1],ni]
    #print(reverseFraction)

print(continuedFraction([5,2]))

#print("17=", lsb(17))
#print("2=", lsb(2))
#print("3=", lsb(3))
#print("4=", lsb(4))
#print("1=", lsb(1))

