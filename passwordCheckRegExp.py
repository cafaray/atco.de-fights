def passwordCheckRegExp(inputString):
    if len(inputString)<5:
        return False
    cl=False
    sl=False
    od=False
    for c in inputString:
        if 'A'<=c<='Z':
            cl=True
        if 'a'<=c<='z':
            sl=True
        if '0'<=c<='9':
            od=True
    return cl and sl and od