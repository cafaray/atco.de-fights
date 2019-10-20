def findSquareSide(x, y):
    d1=((x[1]-x[0])**2)+((y[1]-y[0])**2)
    d2=((x[2]-x[1])**2)+((y[2]-y[1])**2)
    return min(d1,d2)