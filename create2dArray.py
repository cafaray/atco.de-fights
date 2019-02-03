def create2DArray(lengths):
    res=[]
    for i in lengths:        
        res+=[[x for x in range(i)]]
    return res
