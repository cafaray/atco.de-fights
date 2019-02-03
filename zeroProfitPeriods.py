def zeroProfitPeriods(transactions):
    v=0    
    def fp(i):
        t = 0
        for x in range(i,-1,-1):
            if transactions[x]==0: return 0
            t+=transactions[x]
            print(i,t,v)
            if t==v:
                return 1
            elif t>v:
                return 0
            else:
                continue
        return 0
    
    p=0
    c = False    
    for i in range(len(transactions)):
        if transactions[i]==0:
            p+=1
        elif c:
            p+=fp(i-1)
        else:
            continue
    return p

transactions= [-3, -3, 6, 3, 1, 0, -8]
print(zeroProfitPeriods(transactions))