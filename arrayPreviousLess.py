def arrayPreviousLess(items):
    r=[-1]
    for i in range(1,len(items)):
        j=i-1
        e=-1
        while j>=0:            
            if items[j]<items[i]:
                e = items[j]
                break
            j-=1    
        r+=[e]        
    return r