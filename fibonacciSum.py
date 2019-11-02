def fibonacciSum(n):
    f,x=[0,1],1
    while True:
        if f[x-1]+f[x]<=n:
            f+=[f[x-1]+f[x]]
            x+=1
        else:
            break
    r=[f[len(f)-1]]
    #print("numbers:", f)
    #print("first approach:", r)
    s=0
    for x in range(len(f)-2, 1,-1):        
        if sum(r)+f[x]<=n:
            r+=[f[x]]            
        if sum(r)==n:
            return r[::-1]
    return []


n=20
expected=[2, 5, 13]
r=fibonacciSum(n)
print("Assertiopn about n is: ", n, expected, expected==r)

n=21
expected=[21]
r=fibonacciSum(n)
print("Assertiopn about n is: ", n, expected, expected==r)

n=33
expected = [1, 3, 8, 21]
r=fibonacciSum(n)
print("Assertiopn about n is: ", n, expected, expected==r)