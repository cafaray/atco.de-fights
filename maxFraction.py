def maxFraction(numerators, denominators):
    res = []
    for x in range(len(numerators)):
        res += [[numerators[x]/denominators[x],x]]
    return max(res)[1]