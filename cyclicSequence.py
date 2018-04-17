def cyclicSequence(sequence):    
    i = sequence.index(min(sequence))
    seq = []
    for x in range(i, len(sequence)+i):
        pos = x if x < len(sequence) else x - len(sequence)
        seq += [sequence[pos]]
    for x in range(len(seq)-1):
        if seq[x] >= seq[x+1]:
            return False
    return True