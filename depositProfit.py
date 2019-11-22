def depositProfit(deposit, rate, threshold):
    nd = deposit
    for x in range(1,100):        
        nd = nd * (1 + (rate/100))
        print(x, nd)
        if nd >= threshold:
            return x


# best rate time:
data=eval(dir()[0])
data[1]=(data[1]/100)+1
data[0]*=(data[1])
x=1
while data[0]<data[2]:        
    data[0]*=(data[1])        
    x+=1
return x