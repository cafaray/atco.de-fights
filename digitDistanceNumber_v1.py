n=eval(dir()[0])[0]
r=''
while n>=10:
    d=(n%10)
    n/=10
    r+=str(abs(d-n%10))
return int(r[::-1])