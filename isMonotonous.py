def isMonotonous(sequence):    
    monotonous = True
    for x in range(1,len(sequence)):
        if sequence[x-1] >= sequence[x]:
            monotonous = False
            break
    if not monotonous:
        monotonous = True
        for x in range(1,len(sequence)):
            if sequence[x-1] <= sequence[x]:
                return False
    return True