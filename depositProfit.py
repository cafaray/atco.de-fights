def depositProfit(deposit, rate, threshold):
    nd = deposit
    for x in range(1,100):
        
        nd = nd * (1 + (rate/100))
        print(x, nd)
        if nd >= threshold:
            return x