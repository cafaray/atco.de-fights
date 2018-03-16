def primeFactors2(n):
    res = []
    f = set()
    for x in range(2, n+ 1):
        if n % x == 0:
            p = True
            for y in f:
                if x % y == 0:
                    p = False
                    break
            if p:
                f.add(x)
                res.append(x)
    return res