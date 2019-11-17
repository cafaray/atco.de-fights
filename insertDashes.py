def insertDashes(inputString):
    r=''
    for c in inputString:
        if c!=' ':
            r+=c+'-'
        else:
            r=r[:len(r)-1]
            r+=' '
    return r[:len(r)-1]