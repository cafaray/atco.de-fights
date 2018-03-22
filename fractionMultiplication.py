def fractionMultiplication(a, b):
    fraction = [a[0] * b[0], a[1] * b[1]]
    def gcd(a, b):
        if a > b:
            return gcd(b, a)
        if a == 0:
            return b
        return gcd(b % a, a)

    commonDivisor = gcd(fraction[0], fraction[1])
    fraction[0] /= commonDivisor
    fraction[1] /=  commonDivisor 

    return fraction