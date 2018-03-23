def digitDegree(n):
    number = n
    iteracion = 0
    while number > 9:
        cadena = str(number)
        number = 0
        print('cadena:', cadena)
        for c in range(0,len(cadena)):
            number += int(cadena[c])
        print('number:', number)
        iteracion += 1
    return iteracion