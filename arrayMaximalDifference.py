def arrayMaximalDifference(inputArray):    
    md=[]
    for x in range(len(inputArray)):
        for y in range(len(inputArray)):
            md+=[inputArray[x]-inputArray[y]]
    return max(md)