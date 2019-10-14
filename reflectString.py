def reflectString(inputString):
    k=''.join([chr(int((27-(ord(i)-96))+96)) for i in inputString])
    for i in inputString:
        k+=chr(int((27-(ord(i)-96))+96))
    return k