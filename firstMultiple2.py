def firstMultiple2(divisors, start):
    f = start 
    while True:
        for x in divisors:
            if f%x==0:
                return f
        f += 1