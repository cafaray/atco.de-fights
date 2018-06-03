def newNumeralSystem(number):
    res = []
    n = ord(number) - 65 
    for x in range(0,26):
        for y in range(0,26):
            if x+y ==n and x<=y:
                res+=[chr(65+x) + ' + ' + chr(65+y)]
    return res
