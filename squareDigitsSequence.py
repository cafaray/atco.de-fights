def squareDigitsSequence(a0):
    nn = [a0]
    while True:
        snn = str(nn[-1])                
        nv = sum([int(x)**2 for x in snn])        
        if nv not in nn:
            nn += [nv] 
        else:
            break 
    return len(nn)+1

def squareDigitsSequence(a0):    
    nn = [a0]
    while True:
        a=nn[-1] 
        s=0
        while a>0:
            s+=(a%10)**2
            a/=10
        if s not in nn:
            nn+=[s] 
        else:
            break 
    return len(nn)+1