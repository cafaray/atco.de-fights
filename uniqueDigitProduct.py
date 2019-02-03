def uniqueDigitProducts(a):
    
    z = set()
    for c in a:        
        r = 1
        s = str(c)
        for x in s:
            r *= int(x)
        z.add(r)   
    return len(list(z))