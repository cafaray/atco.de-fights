def appleBoxes(k):
    y = [x**2 for x in range(k) if x%2!=0]
    r = [x**2 for x in range(k) if x%2==0]
    return sum(r) - sum(y)