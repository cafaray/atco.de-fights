def isLuckyNumber(n):
    return all(i in ("4", "7") for i in str(n))
