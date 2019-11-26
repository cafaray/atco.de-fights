def isSum(value):
    s = 0
    for x in range(0,value+1):
        s += x
        if s == value:
            return True
        elif s > value:
            return False
    return False

def isSum_optimized(value):
    s,x=0,0
    while s<value:
        x+=1 
        s+=x
        if s==value:return True
    return False


# another way:
v=eval(dir()[0])[0]
s,x=0,0
while s!=v:
    x+=1 
    s+=x
    if s>v:return False
return True