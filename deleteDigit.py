def deleteDigit(n):
    numeros = list()
    cadena = str(n)
    
    numeros = [e for e in cadena]
    print(numeros)
    strNumeros = list()
    for index in range(0, len(numeros)):
        newCadena = ''
        for e in range(0,len(numeros)):
            if index != e:
                newCadena += numeros[e]
                print(newCadena)
        strNumeros.append(int(newCadena))
    print(strNumeros)
    return max(strNumeros)