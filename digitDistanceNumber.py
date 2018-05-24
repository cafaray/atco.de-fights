def digitDistanceNumber(n):
    s = str(n)
    t = ''
    for x in range(1, len(s)):
        t+= str(abs(int(s[x]) - int(s[x-1])))
    return int(t)