def quasifactorial(n):
    result = 1
    for i in range(2,n+1):
        result = (result * i)-1
    return result

