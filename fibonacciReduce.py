from functools import reduce

def fibonacciReduce(n):
    return reduce(lambda x,n: x+[x[-1]+x[-2]], range(n-2), [0,1])

print(fibonacciReduce(6))