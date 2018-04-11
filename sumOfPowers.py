def sumOfPowers(n, divisor):
    res = 0
    for x in range(1,n+1):
        while True:
            if x % divisor == 0:
                res += 1
                x /= divisor
            else: break
    return res