def arrayMaximalAdjacentDifference(inputArray):
    mx=0
    for i in range(len(inputArray)-1):    
        if abs(inputArray[i]-inputArray[i+1])>mx:
            mx= abs(inputArray[i]-inputArray[i+1])
    return mx

def oneline_arrayMaximalAdjacentDifference(inputArray):
    return max([abs(inputArray[i]-inputArray[i+1]) for i in range(len(inputArray)-1)])

# Codefights solution for less chars:
#  a=eval(dir()[0])[0]
#  return max([abs(a[i]-a[i+1]) for i in range(len(a)-1)])