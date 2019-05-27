def walkRobot(data, instructions):
    print(data)
    print(instructions)
    matrix=[]
    for row in range(data[1]):        
        matrix += [[]] 
        for col in range(data[2]):
            matrix[row] += [False]
            if row==data[3]-1 and col==data[4]-1:
                print('startpoint:', row, col)
                matrix[row][col] = True

    for m in matrix:
        print(m)



data = [5, 3, 6, 2, 3]
movements = "EEWNS"
expected = "Case #1: 3 2"
print(walkRobot(data, movements))

data = [4, 3, 3, 1, 1]
movements = "SESE"
expected = "Case #2: 3 3"

data = [11, 5, 8, 3, 4]
movements = "NEESSWWNESE"
expected = "Case #3: 3 7"
