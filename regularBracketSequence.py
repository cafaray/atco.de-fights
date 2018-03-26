def regularBracketSequence1(sequence):
    b = 0
    for x in sequence:
        if x==')': b-=1 
        else: b+=1 
        if b<0: return 0 
    return b == 0