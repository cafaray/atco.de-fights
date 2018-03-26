def isSumOfConsecutive(n):
    for x in range(n):
        suma = 0
        for y in range(x,n):
            suma += y
            if suma == n:
                return True
            if suma > n:
                break
    return False