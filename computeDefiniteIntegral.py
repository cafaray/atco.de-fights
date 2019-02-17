def computeDefiniteIntegral(l, r, p):
    di1, di2 = 0,0
    for x in range(len(p),0,-1):
        di1 += p[x-1]*((r**x)/x)
        di2 += p[x-1]*((l**x)/x)        
    return di1-di2