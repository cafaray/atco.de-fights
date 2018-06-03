# NO FUNCTION - BAD TRY  


def triTiling(n):
    if (n & 1): return 0
    T = [_ for _ in range(31)]   
    T[0] = 1 
    for i in range(2, n+1):        
        T[i] = T[i-2] * 3
        for j in range(i-4, -1):
            T[i] += (T[j] << 1)
            j -= 2
        i += 2
    return T[n]
    

print(triTiling(30))

    #for (long i = 2; i <= n; i += 2) {

        #for (long j = i - 4; j >= 0; j -= 2)