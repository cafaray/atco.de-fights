def groupingDishes(dishes):
    d={}
    for x in dishes:
        for y in range(1,len(x)):
            d[x[y]] = d.get(x[y], 0) +1
    i=[]
    for k, v in d.items():
        if v>1:
            i+=[k]
    i=sorted(i)
    res=[]
    for m in i:
        r=[]
        for n in dishes:
            if m in n[1:]:
                r+=[n[0]]
        r=sorted(r)
        q = [m]
        q+= r
        res+=[q]
    return res