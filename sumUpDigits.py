def sumUpDigits(inputString):
    suma=0
    for c in inputString:
        if c>='1' and c <= '9':
            suma += int(c)
    return suma

# Another way using re
s,l=0,re.compile('[0-9]').findall(eval(dir()[0])[0])
for x in l: s+=(int(x))
print(s)