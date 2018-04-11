def swapCase(text):
    nt = ''
    for x in text:
        if x >= 'A' and x <= 'Z':
           nt += x.lower()
        elif x >= 'a' and x <= 'z':
           nt += x.upper()
        else:
            nt += x
    return nt