import math
def factorPrime(n):
    
    def primes(n):
        noprimes = set(j for i in range(2, n) for j in range(i*2, n, i))
        prime = [x for x in range(2,n+1) if x not in noprimes]
        return prime
    d = primes(n//2)
    p = dict((el,0) for el in d)
    for k,v in p.items():
        while n>1:
            if n%k==0:
                p[k] = p.get(k,0)+1
                n=n//k
            else:
                break
    return p

#    results = set()
#    step = 2 if n%2 else 1
#    for i in range(1, int(math.sqrt(n)) + 1, step):
#        if n%i == 0:
#            results.add(i)
#            results.add(int(n/i))
#    res = sorted(list(results))
#    return res[1:len(res)-1]
            
print(factorPrime(237))