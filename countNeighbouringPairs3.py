c = p = 0
for x in eval(dir()[0])[0]:
    c += p == x
    p = x
return c