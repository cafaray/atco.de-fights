def maxZeros(n):
    res = 0
    mZeros = 0
    for k in range(2,n+1):
        nZeros = 0
        val = n
        while val != 0:
            if val % k == 0:
                nZeros += 1
            val = val // k

        if nZeros > mZeros:
            mZeros = nZeros
            res = k
    return res 
