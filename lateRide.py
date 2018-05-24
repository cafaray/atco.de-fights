def lateRide(n):
    h = n // 60
    if n%60==0: return h
    m = n - (h*60)
    strNumber = str(h) + str(m)
    return sum([0] + [int(x) for x in strNumber])