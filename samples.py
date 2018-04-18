def printMatrix(s, n):
    if len(s)!=n**2:
        print("Impossible create a irregular matrix")

    for x in range(1,n+1):
        print('[')
        for y in range(x*n-1,n*x):
            print(s[x-1+y])
        print(']')

printMatrix('123456789', 3)