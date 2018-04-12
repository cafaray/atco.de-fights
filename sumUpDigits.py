def sumUpDigits(inputString):
    suma=0
    for c in inputString:
        if c>='1' and c <= '9':
            suma += int(c)
    return suma