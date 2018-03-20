def reflectString(inputString):
    k=''
    for i in inputString:
        k+=chr(int((27-(ord(i)-96))+96))
    return k