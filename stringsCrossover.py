def stringsCrossover(a, result):
    res = 0
    for i in range(len(a)-1):
        for j in range(len(a)):
            yeap = True
            k = 0
            while k < len(result) and yeap:
                yeap &= (result[k] == a[i][k] or result[k] == a[j][k])
                k+=1            
            res += 1 if yeap else 0
            j += 1
        i += 1
    return res;