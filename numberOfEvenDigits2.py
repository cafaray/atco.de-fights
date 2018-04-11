def numberOfEvenDigits(n):
    result = 0
    while n != 0:
        if n % 2 == 0:
            result += 1
        n //=  10
    return result