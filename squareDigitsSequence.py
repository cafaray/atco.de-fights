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