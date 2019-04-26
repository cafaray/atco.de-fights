def isPrime(x):
    if x==1: return False
    if x==2: return True
    if x%2==0: return False
    if x==3: return True
    i = 3
    while True:
        if i*i>x: break 
        if x%i==0: return False
        i+=2
    return True