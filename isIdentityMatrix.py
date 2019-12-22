def isIdentityMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==j: 
                if matrix[i][j]==1:
                    continue
                else:
                    return False
            if matrix[i][j]!=0:
                return False
    return True

matrix=[[1,0,0], [0,1,0], [0,0,1]]
e=True
#r=isIdentityMatrix(matrix)
#print("Assertion for test case 1 is: ", e==r)

matrix=[[1,0,0], 
[0,0,0], 
[0,0,1]]
e=False
r=isIdentityMatrix(matrix)
print("Assertion for test case 2 is: ", e==r)
