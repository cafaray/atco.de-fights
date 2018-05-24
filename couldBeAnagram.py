def couldBeAnagram(s1, s2):
    if len(s1)!=len(s2): return False
    ac1 = ''.join(sorted(list(s1)))
    ac2 = ''.join(sorted(list(s2)))
    #if ac1==ac2: return True
    pair = len(ac2)
    tmp = ''
    comodin = cuentaComodines(ac1)
    lx = comodin-1
    for y in range(len(ac2)):
        for x in range(lx, len(ac1)):
            if ac2[y]==ac1[x] and str(y) not in tmp:
                tmp += str(y)
                pair-=1
                lx = x
                break
    return pair == comodin

def cuentaComodines(ac1):
    comodin = 0
    for x in ac1:
        if x=='?':
            comodin+=1
        else:
            break
    return comodin