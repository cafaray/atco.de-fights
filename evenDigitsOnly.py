def evenDigitsOnly(n):
    s = str(n)
    for c in s:
        if int(c)%2!=0:
            return False
    return True
