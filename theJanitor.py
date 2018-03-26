def theJanitor(word):
    l = [0] * 26
    r = [0] * 26
    was = [0] * 26
    for x in range(26):
        l+=[0]
        r+=[0]
        was += [False]

    for x in range(len(word)):
        c = ord(word[x]) - ord('a')
        if not was[c]:
            l[c] = x
            was[c] = True
        r[c] = x

    res = []
    for x in range(26):
        res+=[r[x] - l[x] + 1 if was[x] else 0]
    return res