def extraNumber(a, b, c):
    d = {}
    d[a] = d.get(a, 0) + 1
    d[b] = d.get(b, 0) + 1
    d[c] = d.get(c, 0) + 1
    for k,v in d.items():
        if v < 2:
            return k