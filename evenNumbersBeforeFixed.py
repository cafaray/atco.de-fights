def evenNumbersBeforeFixed(sequence, fixedElement):
    if fixedElement not in sequence: return -1
    res = []
    for x in range(len(sequence)):
        if sequence[x] == fixedElement: break
        if sequence[x]%2==0:
            res += [sequence[x]]
    return len(res)