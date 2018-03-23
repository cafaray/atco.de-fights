import re
def isBeautifulString(inputString):
    orderedString = sorted(inputString)
    inputString = ""
    for c in orderedString:
        inputString += c
    #inputString = str(inputString)
    print(inputString)
    count = len(inputString)
    esPrimero = True
    previo = ''
    for caracter in range(ord('a'),ord('z')+1): #inputString:
        char = chr(caracter)
        print(char)
        pattern = re.compile(char)
        res = pattern.findall(inputString)        
        #print(res)
        if esPrimero is False:
            if count < len(res): 
                return False
            else:
                count = len(res)
                previo = caracter
        else:
            count = len(res)
            previo = caracter
            esPrimero = False
    return True