def primeFactors2(n):
    r = []
    i = 2
    while i * i <= n:
        j = 1
        while n % i < 1: 
            r += [i] * j
            j = 0
            n /= i  
        i += i%2+1
        
    return r + [n] * (n > 1)  # the key of the optimization for this excersise is [n] * (n>1)

test= primeFactors2(100)
expected = [2, 5]
print('Assertion: ', test, ' = [2, 5]', test==expected)