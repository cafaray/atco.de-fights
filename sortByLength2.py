import operator

def sortByLength(inputArray):
    s = [len(inputArray[x]) for x in range(len(inputArray))]
    d = dict()
    for e in range(len(s)):
        d[e] = s[e]
    d = sorted(d.items(), key=operator.itemgetter(1))
    i=[]
    for e in d:
        i+=[inputArray[e[0]]]
    return i