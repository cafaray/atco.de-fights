def josephusProblem(n, k):

    removed = [False for _ in range(n)]
    currentPerson = 0

    for i in range(n-1):
        skipped = 0
        while skipped < k - 1:
            if not removed[currentPerson]:
                skipped+=1
            currentPerson = (currentPerson+1) % n
        
        while removed[currentPerson]:
            currentPerson = (currentPerson+1) % n
        
        removed[currentPerson] = True

    for i in range(n):
        if not removed[i]:
            return i + 1

    return 0

print(josephusProblem(10, 4))