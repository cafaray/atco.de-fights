def digitDistanceNumber(n):
    s = str(n)
    t = ''
    for x in range(1, len(s)):
        t+= str(abs(int(s[x]) - int(s[x-1])))
    return int(t)


def digitDistanceNumber1(n):
    s=str(n)
    b=''
    for x in range(1,len(s)):
        b+=str(abs(int(s[x-1])-int(s[x])))
    return int(b)