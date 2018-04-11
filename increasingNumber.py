def increasingNumber(x, n):    
    for y in range(1, n+1):
        while x % y != 0:
            x++
    return x