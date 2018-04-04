def fibonacciIndex(n):
    x = 0
    y = 1
    c = 0
    index = 0
    if n <= 1: return index
    while c < n:
        z = x + y
        x = y
        y = z
        c = len(str(z))
        index += 1
    return index + 1