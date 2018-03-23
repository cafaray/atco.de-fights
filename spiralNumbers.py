def spiralNumbers(n):
    width, height = n, n
    x, y = width // 2, height // 2 # inicia al centro    
    N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # Define los sentidos
    turn_right = {N: W, W: S, S: E, E: N} # mapa de camino viejo -> nueva direccion para el caso de no pares (3, 5, 7, ...)
    dx, dy = N # la direccion inicial es N para ir en el flujo; N - W - S - E
    if n%2 == 0: # cuando es par, cambia el sentido a S - E - N - W
        x -= 1
        turn_right = {S: E, E: N, N: W, W: S} 
        dx, dy = S # la direccion inicial sera entonces S

    matrix = [[None] * width for _ in range(height)]
    count = width * height
    while True:
        matrix[y][x] = count 
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # mueve hasta alcanzar el limite para cambio de direccion
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # se ha terminado, llegamos a 1.
        count -= 1