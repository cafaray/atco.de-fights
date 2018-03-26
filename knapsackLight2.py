def knapsackLight2(weight1, weight2, maxW):
    if weight1 > maxW and weight2 > maxW: return "none"   
    if weight1 + weight2 <= maxW: return "both"
    if weight1 <= maxW and weight2 <= maxW: return "either"
    if weight2 <= maxW: return "second"
    return "first"