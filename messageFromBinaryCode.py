def messageFromBinaryCode(code):
    return ''.join([chr(int(code[8* (x-1):8*x],2)) for x in range(1, (int(len(code) / 8))+1)])
