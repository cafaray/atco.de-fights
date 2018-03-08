def numberOfEvenDigits(n):
    increase = 0
    strn = str(n)
    for x in strn:
        if int(x)%2==0:
            increase += 1
    return increase