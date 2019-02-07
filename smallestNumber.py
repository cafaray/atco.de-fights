def smallestNumber(n):    
    m = ['0']*n
    if len(m)>1:
        m[0] = '1'
    else:
        return 0
    return int(''.join(m))