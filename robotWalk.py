def robotWalk(a):
    return any(a[i] >= a[i-2] for i in range(3, len(a)))