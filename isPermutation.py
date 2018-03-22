def isPermutation(n, inputArray):
    x = n
    c = 0
    for z in range(len(inputArray)):
        if inputArray[z]==x:
            c +=1
            x -=1
            z = 0
            continue
        z +=1
    
    return c == n
    