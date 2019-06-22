# def minimalNumberOfCoins(coins, price):
params=eval(dir()[0])
c,p,m=params[0], params[1],0
for i in range(len(c)-1,-1,-1):
    m+=p//c[i]
    p=p%c[i]
    if p<=0: break
return m