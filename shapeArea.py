def shapeArea(n):    
    a = 2 * n - 1    
    for i in range(n-1,0,-1):
        a += 2*((i*2)-1)
    return a