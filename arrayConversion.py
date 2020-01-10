def arrayConversion(inputArray):
    x=1
    while len(inputArray)>1:
        r=[]
        for i in range(0,len(inputArray),2):
            if x%2==0:
                r+=[inputArray[i]*inputArray[i+1]]
            else:
                r+=[inputArray[i]+inputArray[i+1]]
        x+=1
        inputArray = r
    return inputArray[0]