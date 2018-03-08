def alternatingSums(a):
    return [sum([a[x] for x in range(len(a)) if x%2==0])] + [sum([a[x] for x in range(len(a)) if x%2!=0])]