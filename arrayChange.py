def arrayChange(inputArray):
    c=0
    for i in range(1,len(inputArray)):    
        if inputArray[i-1]>=inputArray[i]:
            c+=((inputArray[i-1]+1)-inputArray[i])
            inputArray[i]=inputArray[i-1]+1                    
    return c