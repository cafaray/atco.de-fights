def fixedPointsPermutation(permutation):

    result = 0
    for i in range(len(permutation)):
        if i+1 == permutation[i]:
            result += 1

    return result