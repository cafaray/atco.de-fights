def cyclicString(s):
    c = len(s)
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            a=s[i:j]
            n= len(s) // len(a) + 1
            if s in a*n and c > len(a):
                c = len(a)
    return c