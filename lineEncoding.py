def lineEncoding(s):
    cadena = ''
    suma = 1
    for c in range(0, len(s)):
        if c + 1 == len(s):
            if s[c] != s[c-1]:
                suma = 1
        else:
            if s[c] == s[c+1]:
                suma += 1
                continue
            
        if suma > 1:
            cadena += str(suma)+s[c]
        else:
            cadena += s[c]
        suma = 1
    return cadena