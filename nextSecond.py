def nextSecond(currentTime):

    #no pass all test, reviews
    currentTime[0] += 1
    currentTime[1] += 1
    currentTime[2] += 1
    if currentTime[0] == 24:
        currentTime[0] = 0
    elif currentTime[1] == 60:
        currentTime[1] = 0
    elif currentTime[2] == 60:
        currentTime[2] = 0
    return currentTime