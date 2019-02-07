def sameDigitNumber(n):
    s = str(n)
    for x in range(1, len(s)):
        if s[x]!=s[x-1]:
            return False
    return True