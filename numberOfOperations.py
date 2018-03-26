def numberOfOperations(a, b):
    c = 0
    while a%b==0 or b%a==0:
        print(a, b)
        if a>b:
            a = a/b
            c += 1
        else:
            b = b/a
            c += 1
    return c

print(numberOfOperations(432, 72))
