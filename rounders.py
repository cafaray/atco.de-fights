def rounders(value):
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