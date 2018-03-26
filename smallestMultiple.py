def smallestMultiple(left, right):
    ints = [x for x in range(left,right+1)]
    print(ints)
    x = ints[-1]
    while True:
        isDiv = True
        for y in ints:
            if x%y!=0:
                isDiv = False
                break
        if isDiv: return x
        x+=1