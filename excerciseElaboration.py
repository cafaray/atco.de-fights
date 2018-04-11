def exerciseElaboration(p, n):
    s = str(p) + n*'0' + str(p)
    i = int(s)**2
    s = str(i)
    suma = 0
    for c in s:
        suma += i