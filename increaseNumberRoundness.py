def increaseNumberRoundness(n):
    strn = str(n)[::-1]
    f0 = False
    for s in strn:
        if s == '0' and f0:
            return True
        else:
            if s!='0':
                f0 = True
    return False