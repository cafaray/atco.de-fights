    res = list()
    for a in choices:       
        if a[0] < a[1] and a[0] not in res:
            res.append(a[0])
            continue
        elif a[0] >= a[1] and a[1] not in res:
            res.append(a[1])
            continue    
        else:            
            c = Counter(res)
            if c[a[0]] <= c[a[1]]:
                res.append(a[0])
            else:
                res.append(a[1])
    return res




    from collections import Counter
def leastAppearance(choices):
    res = {}
    #i = 0
    for a in range(len(choices)):
        #if len(res) <= 0:
        #    if choices[a][0]<choices[a][1]:
        #        res[a] = choices[a][0]
        #    else:
        #        res[a] = choices[a][1]
        #else:
        c = Counter(res.values())
        if c[choices[a][0]] <= c[choices[a][1]]:
            res[a] = choices[a][0]
        else:
            res[a] = choices[a][1]        
    return list(res.values())
