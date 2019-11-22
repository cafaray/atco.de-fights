def checkEqualFrequency(inputArray):
    s=sorted(inputArray)
    c,d=1,1
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            c+=1
        else:
            break
    print("repeticiones: ", c)
    if c==1: return True
    if len(s)%c!=0: return False
    nc=1    
    for i in range(c+1,len(s)):
        if s[i]==s[i-1]:
            nc+=1
        else:
            if nc!=c:
                return False
    return True

inputArray= [1, 2, 2, 1]
e=True

inputArray=[1, 2, 2, 3, 1, 3, 1, 3]
e=False

inputArray=[239]
e=False

inputArray=[239, 240, 241]
e=True

inputArray=[34, 23, 33, 23]
e=False

inputArray=[1, 1, 1, 1, 1]
e=True

inputArray=[1, 1, 1, 2]
e=False

inputArray=[100000000, 400000000, 200000000, 400000000, 200000000, 100000000]
e=True

inputArray=[19, 33, 33, 23]
e=False
r=checkEqualFrequency(inputArray)
print("Assertion at eval 9,", r==e)

inputArray=[2, 2, 2, 1, 1]
e=False

inputArray=[1, 3, 1, 2, 3, 2, 1, 2, 3]
e=True

