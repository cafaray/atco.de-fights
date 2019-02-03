def primesSum(a, b):
    return sum([a for a in range(a,b+1) if not (a<2 or any(a%x==0 for x in range(2, int(a**0.5)+1)))])

print(primesSum(10,20))