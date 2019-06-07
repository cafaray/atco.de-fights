import operator

def firstNotRepeatingCharacter(s):
    d={}
    for c in s:
        d[c]=d.get(c,0)+1        
    sorted_d = sorted(d.items(), key=operator.itemgetter(1))
    return sorted_d[0][0] if sorted_d[0][1]==1 else '_'