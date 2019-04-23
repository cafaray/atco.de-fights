class Prizes(object):
    def __init__(self, purchases, step, divisible):
        self.my = [x+1 for x in range(step-1,len(purchases),step) if purchases[x]%divisible==0]
        print(self.my)
        #self.step = step
        #self.divisible = divisible
        self.i = 0

    def __iter__(self):         
        return self                
        
    def __next__(self):
        if self.i>=len(self.my):
            raise StopIteration
        else:
            self.i+=1
            return self.my[self.i-1]
        
        
def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))

purchases = [12, 43, 13, 465, 1, 13]
n=2
d=3
print(superPrize(purchases, n, d))