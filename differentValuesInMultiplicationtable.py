def differentValuesInMultiplicationTable(n, m):
    return len(set([[i*j for j in range(1,m+1)] for i in range(1,1+n)]))