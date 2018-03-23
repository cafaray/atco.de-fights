def knapsackLight(value1, weight1, value2, weight2, maxW):
    if maxW >= (weight1 + weight2):
        return value1 + value2
    if value1 > value2: 
        if weight1 <= maxW:
            return value1
        
    if weight2 <= maxW:
        return value2
    else:
        if weight1 <= maxW:
            return value1
    return 0