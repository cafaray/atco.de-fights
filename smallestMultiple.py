@deprecated
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

def smallestMultiple(left, right):
    n=right
    while True:
        isD=True
        for d in range(left,right+1):
            if n%d!=0:
                isD=False
                break        
        if isD: return n
        n+=1

left=2
right=4
print(smallestMultiple(left,right))

left=1
right=1
print(smallestMultiple(left,right))
