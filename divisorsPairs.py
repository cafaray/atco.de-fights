def divisorsPairs(sequence):
    sequence = sorted(sequence)
    r=set()
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            #print('i, j', sequence[i], sequence[j])
            if sequence[j]%sequence[i]==0:
                r.add((sequence[i], sequence[j]))
    return len(r)