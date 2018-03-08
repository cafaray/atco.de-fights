def specialPolynomial(x, n):
    num = 0
    for k in range(n):
        num+=x**k
        print(num)
        if num>n:
            return k-1
        if num==n:
            return k