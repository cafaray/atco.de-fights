def divNumber(k, l, r):
    ans = 0
    for i in range(l, r + 1):
        n = i
        divisor = 1
        j = 2
        while j * j <= n:
            pow2 = 0
            while n % j == 0:
                n /= j
                pow2 += 1
            divisor *= 1 + pow2
            if divisor > k:
                break
            j += 1
        if n > 1:
            divisor *= 2
        if divisor == k:
            ans += 1
    return ans

def divNumber(k, l, r):
    f=0
    for n in range(l,r+1):
        d,i=0,1
        while i<=n:
            if n%i==0:d+=1
            if d>k:break
            i+=1
        if d==k:f+=1
    return f