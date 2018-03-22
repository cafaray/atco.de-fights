def comfortableNumbers(l, r):
    pairs = 0
    for i in range(l, r+1):  #fuck, me faltaba incluir el valor final
        for j in range(i+1, r+1): #fuck, me faltaba incluir el valor final
            sa = s(i)
            sb = s(j)
            if j>=(i-sa) and j<= (i+sa) and i>= (j-sb) and i <= (j+sb):
                pairs += 1    
    return pairs
    
def s(x):
    itera = 0
    while x:
        itera += x%10
        x = x//10
    return itera