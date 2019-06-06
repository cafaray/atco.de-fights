def sudoku2(grid):
    for x in range(len(grid)):
        s = set()
        for y in range(len(grid[x])):
            if grid[x][y]=='.':
                continue
            if grid[x][y] not in s:
                s.add(grid[x][y])
                continue
            return False
    for y in range(len(grid[0])):
        s = set()
        for x in range(len(grid)):
            if grid[x][y]=='.':
                continue
            if grid[x][y] not in s:
                s.add(grid[x][y])
                continue
            return False
    return reviewSquares(grid)

def reviewSquares(grid):
    o,r,c=0,0,0
    s=set()
    while r < len(grid):
        o=r
        s = set()
        while c < len(grid[r-1]):                                   
            if grid[r][c] in s and grid[r][c]!='.':
                return False    
            s.add(grid[r][c])
            c+=1
            if (c)%3==0:
                r+=1
                if (r)%3==0:
                    if c<len(grid[r-1]): 
                        r=o
                    else:                        
                        c=0
                    break
                else:
                    c-=3
    return True

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
print(sudoku2(grid))