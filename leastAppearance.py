from collections import Counter
def leastAppearance(choices):
    res = {}
    for a in range(len(choices)):
        c=Counter(res.values())
        if c[choices[a][0]]<=c[choices[a][1]]:
            res[a]=choices[a][0]
        else:
            res[a]=choices[a][1]
    return list(res.values())


def leastAppearance(choices):
    c,r=dict(),[]
    for a in choices:
        if a[0]<a[1] and c.get(a[0],0)<=c.get(a[1],0):
            r+=[a[0]]
            c[a[0]]=c.get(a[0],0)+1
        else:
            r+=[a[1]]
            c[a[1]]=c.get(a[1],0)+1
    return r