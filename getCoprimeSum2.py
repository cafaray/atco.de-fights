def getCoprimeSum(n):
    phi = [0 for x in range(n+1)]
    s = 0
    phi[1] = 1
    i = 2
    while i < n:
        if phi[i] == 0:
            phi[i] = i - 1
            j = 2
            while j * i < n:
                if phi[j] != 0:
                    q = j
                    f = i - 1
                    while q % i == 0:
                        f *= i
                        q //= i
                    phi[i * j] = f * phi[q]
                j += 1        
        s += phi[i]
        i += 1
    print(phi)
    return s%1000000007

print(getCoprimeSum(237))