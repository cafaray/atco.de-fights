def fixedPointsPermutation(permutation):
    
    result = 0

    for i in range(1, len(permutation) + 1):
        if permutation[i] == i + 1:
            result += 1

    return result