def addDigits(a, b, n):
    sd = str(a)
    for x in range(n):
        for y in range(10, -1, -1):
            eval = sd + str(y)
            if int(eval)%b==0:
                sd = sd + str(y)
                break
            else:
                continue
        print('sd',sd)
    return sd