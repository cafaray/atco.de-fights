def weakNumbers(n):    
    divs = []
    for x in range(1, n+1):
        divs += [sum([1 for div in range(x, 0, -1) if x%div==0])]
    lt = []
    for d in range(len(divs), 0, -1):
        lt += [sum([1 for x in range(0, d) if divs[x]>divs[d-1]])]
    return[max(lt), lt.count(max(lt))]