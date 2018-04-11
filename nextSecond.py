def nextSecond(currentTime):

    #no pass all test, reviews
        
    currentTime[2] += 1
    if currentTime[2] == 60:
        currentTime[2] = 0
        currentTime[1] += 1
    
    if currentTime[1] == 60:
        currentTime[1] = 0
        currentTime[0] += 1
        
    if currentTime[0] == 24:
        currentTime[0] = 0
    return currentTime