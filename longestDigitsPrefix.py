def longestDigitsPrefix(inputString):
    salida = ''
    for c in inputString:
        try:
            if int(c) >= 0:
                salida += c
        except:
            return salida
    return salida