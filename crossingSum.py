def crossingSum(matrix, a, b):
    res=0
    max=0    
    for i in range(len(matrix)):   
        res+=matrix[i][b]    
        i+=1
    for j in range(len(matrix[0])):       
        if j==b:
            continue
        res += matrix[a][j] 
        j+=1      
    return res