def reverseToSort(inputArray):    
    def incremental(a):
        for i in range(1,len(a)):
            if a[i-1]<a[i]:
                continue
            else:
                return False
        return True
    a=[]
    i=1
    while i<len(inputArray):
        if inputArray[i-1] < inputArray[i]:
            a+=[inputArray[i-1]]
            i+=1
        elif inputArray[i-1]==inputArray[i]:
            return False
        else:
            s=[]            
            while inputArray[i-1]>inputArray[i]:                
                s+=[inputArray[i-1]]
                i+=1
                if i>=len(inputArray):
                    i-=1
                    break
            s+=[inputArray[i]]                            
            a+=s[::-1]
            
            a+=inputArray[i:]
            break
    return incremental(a)


inputArray=[100, 99, 98]
e=True
print("Assetion for test case 8: ", e==reverseToSort(inputArray))

inputArray=[19, 32, 23]
e=True
print("Assetion for test case 4: ", e==reverseToSort(inputArray))

inputArray=[-1, 5, 4, 3, 2, 8]
e=True
print("Assetion for test case 1: ", e==reverseToSort(inputArray))