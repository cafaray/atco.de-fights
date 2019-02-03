import math
def derivatePolynomial(poly, dev): 
    c = 0                                # correction
    r = dev                              # to remove
    while dev > 0:
        for i in range(1, len(poly)-c):
            poly[i-1] = (len(poly)-(i+c))*poly[i-1]
        dev -= 1                                    # I suspect this
        c += 1
        
    print(math.expm1(math.log(4,2)))
    return poly[:-r]



print(derivatePolynomial([1,1,2,6],2))