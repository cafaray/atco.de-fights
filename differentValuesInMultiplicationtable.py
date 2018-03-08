def differentValuesInMultiplicationTable(n, m):

    g = [[i*j for j in range(1,m+1)] for i in range(1,1+n)]
    print(g)
    s = set()
    for i in g:
        s|=set(i)
        print(s)
    return len(s)