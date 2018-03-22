import math
def isPower(n):    
    if n == 1: return True
    base = 2
    while base < n:
        base = base + 1
        power = round(math.log (n, base))
        if power<=1: break
        if base**power==n: return True        
    return False