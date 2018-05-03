def firstNotDivisible(divisors, start):    
    number = start
    yeap = True
    while yeap:
        yeap = False
        for x in divisors:            
            if number % x == 0:
                yeap = True
                break
        number += 1  