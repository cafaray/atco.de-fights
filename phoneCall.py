def phoneCall(min1, min2_10, min11, s):
    if s < min1: return 0
    rest = s - min1
    if rest <= 0: return 1
    if rest <= (9 * min2_10): return (rest // min2_10) + 1
    rest = rest - (9 * min2_10)    
    return 10 + (rest//min11)