def evenNumbersBeforeFixed(sequence, fixedElement):
    r=0
    f=False
    for e in sequence:
        if e==fixedElement:
            f=True
            break
        if e%2==0:
            r+=1
    return -1 if not f else r