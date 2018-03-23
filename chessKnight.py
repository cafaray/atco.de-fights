def chessKnight(cell):
    limits = ['a1', 'a8', 'h1', 'h8']
    if cell in limits: 
        return 2
    
    col = cell[0:1]
    row = cell[1:2]
    print(col + row)
    if col == 'a' or col == 'h':
        print('es a o h')
        if int(row) > 2 and int(row) < 7:
            return 4
        else:
            return 3
    elif col == 'b' or col == 'g':
        print('es b o g')
        if int(row) > 2 and int(row) < 7:
            return 6
        elif int(row) == 2 or int(row) == 7:
            return 4
        else:
            return 3
    else:
        print('es distinto de a o h o b o g')
        print('row es:', int(row))
        if int(row) > 2 and int(row) < 7:
            return 8
        elif int(row) == 2 or int(row) == 7: 
            return 6
        else:
            return 4
    return 8
