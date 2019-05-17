def firstMultiple(divisors, start):
    itDoesnt = False
    while True:
        for divisor in divisors:
            if start%divisor!=0:
                itDoesnt = True
                break
            else:
                itDoesnt = False
        if not itDoesnt: return start
        start+=1