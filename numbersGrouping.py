def numbersGrouping(a):
    ans = []
    for i in range(100000):
        ans.append(0)
    
    l = len(a)
    for i in range(l):
        index = (a[i]-1)//10000
        if ans[index] == 0:
            ans[index] += 2
        else:
            ans[index] += 1
    
    return sum(ans)