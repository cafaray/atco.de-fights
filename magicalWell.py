def magicalWell(a, b, n):
    m = 0
    for i in range(1,n+1):
        m = m + a * b
        a = a+1
        b = b+1
    return m