def chessBoardSquaresUnderQueenAttack(a, b):
    
    def possible(x, y, dx, dy):
        if (x < 0 or x >= a) or (y < 0 or y >= b):
            return 0
        return possible(x+dx, y+dy, dx, dy) + 1
    
    ans = 0
    for i in range(a):
        for j in range(b):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx != 0 or dy != 0:
                        ans += possible(i+dx, j+dy, dx, dy)
    return ans