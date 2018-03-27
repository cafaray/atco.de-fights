def josephusProblem(n, k):
    winners = [x+1 for x in range(n)]
    personas = [True for x in range(n)]
    actual = 0
    while len(personas) > 1:
        print(personas, winners)
        quitar = (k - 1) + actual
        if quitar >= len(personas): 
            quitar = len(personas) - quitar
            print("nuevo quitar:", quitar)
        actual = quitar
        personas[quitar] = False
        winners = [winners[x] for x in range(len(personas)) if personas[x]]
        personas = [True for x in range(len(personas)) if personas[x]]
    print(personas, winners)
    return winners[0]

print(josephusProblem(10, 4))