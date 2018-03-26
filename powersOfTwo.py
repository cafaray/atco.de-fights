def powersOfTwo(n):
    sumas = []
    actual = 1
    print(n, actual)
    while n>0:
        if n%2==1:
            sumas+=[actual]
        n >>= 1
        actual <<= 1
        print(n, actual)
    return sumas