def reverseOddCount(string):
    d = {}
    for c in string:
        if string.count(c) %2!=0:
            d[c] = string.count(c)
    nstr = list(string)
    pos = 0
    for c in range(len(string)-1):        
        if d.get(string[c], 0)>0:
            print('processing:', string[c], pos)
            i = 1
            while (d.get(string[len(string)-i-pos],0) == 0):                
                i+=1
            tmp = string[len(string)-i-pos]            
            nstr[len(string)-i-pos] = string[pos] 
            nstr[pos] = tmp
        pos+=1
    print(nstr)

print(reverseOddCount('hello world'))





l1 = [j for j in range(len(str)) if(str.count(str[j])%2==0)]# [4,7]
res = [None]*len(str)
    
for s in range(len(l1)):
    res.insert(l1[s],str[l1[s]])
j = len(str)-1
for i in range(len(str)):
    if(i in l1):
        pass
    else:
        while(True):
            if(j in l1):
                j-=1
            else:
                break
        res.insert(j,str[i])
        j-=1
        

res = list(filter(None,res))

return "".join(res)