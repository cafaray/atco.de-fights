def areIsomorphic(a1, a2):
    if len(a1) != len(a2): return False
    for i in range(len(a1)):
        if len(a1[i]) != len(a2[i]): return False
    return True