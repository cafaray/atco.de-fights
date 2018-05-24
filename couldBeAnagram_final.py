from collections import Counter
def couldBeAnagram(s1, s2):
    if Counter(s1) == Counter(s2): return True
    comodines = Counter(s1) - Counter(s2)
    diferencias = Counter(s2) - Counter(s1)
    d = 0
    for x,v in diferencias.items():
        d+=v
    return d==comodines['?']
    