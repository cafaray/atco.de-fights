def bfsDistancesUnweightedGraph(matrix, startVertex):
    d=[0]*len(matrix)
    seen=[startVertex]
    queue=[startVertex]
    while queue:
        v=queue.pop(0)
        for i in range(len(matrix)):
            if not i in seen and matrix[v][i]:
                seen.append(i)
                queue.append(i)
                d[i]=d[v]+1
    return d