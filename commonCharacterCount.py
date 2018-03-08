def commonCharacterCount(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    suma = 0
    for x in set1:
        suma += s1.count(x) if s1.count(x) < s2.count(x) else s2.count(x)
    return suma