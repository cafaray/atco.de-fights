def primo(x):
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

def leastCommonPrimeDivisor(a, b):
    aux = -1
    i = 2
    while True:
        if i>min(a, b): break
        if primo(i) and a %i==0 and b%i == 0:
            aux = i
            break
        i+=1
    return aux