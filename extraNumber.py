def extraNumber(a, b, c):
    numbers = sorted([a,b,c])
    if numbers[0] == numbers[1]: return numbers[2]
    return numbers[0]