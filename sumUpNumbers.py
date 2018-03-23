import re
def sumUpNumbers(inputString):
    suma = 0
    m = re.findall("\d+", inputString)
    if m is None: return 0
    #print(m)
    for number in m:
        suma += int(number)
    return suma