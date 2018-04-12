def threeAndFour(n):
    res = []
    for x in range(n):
        if x%3 ==0 and x%4==0:
            res+=[x]
    return res