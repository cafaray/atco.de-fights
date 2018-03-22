def zFunctionNaive(s):
    res = []
    for z in range(len(s)): 
        c = 0
        i = z
        j = 0
        while i < len(s) and j < len(s) and s[i] == s[j]:
            c+=1
            i+=1
            j+=1
        
        res+=[c]
    return res