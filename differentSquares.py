def differentSquares(matrix):
    if len(matrix) <= 1: return 0
    #lista = list()
    myDict = dict()
    for mat in range(0,len(matrix)):
        if len(matrix[mat]) <= 1: return 0
        #print(len(matrix[mat]))
        for n in range(0,len(matrix[mat])+1):
            if mat + 1 >= len(matrix): continue
            if n + 1 >= len(matrix[mat]): break
            #print(matrix[mat][n], matrix[mat][n+1])
            #print(matrix[mat+1][n], matrix[mat+1][n+1])
            #print('========')
            number = (matrix[mat][n], matrix[mat][n+1], matrix[mat+1][n], matrix[mat+1][n+1])
            #lista.append(number)
            myDict[number] = 1
            #print(matrix[mat][n], matrix[mat+1][n])
            
    #print(lista)
    print(myDict)
    return len(myDict)
