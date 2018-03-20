def permutationShift(permutation):
    a = []
    for i,x in enumerate(permutation):
        a.append(x-i)
    return max(a) - min(a)