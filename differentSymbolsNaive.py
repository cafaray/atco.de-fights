def differentSymbolsNaive(s):
    count = dict()
    x = 0
    for character in s:
        count[character] = x
        x = x + 1
    return len(count)