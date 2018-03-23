def growingPlant(upSpeed, downSpeed, desiredHeight):
    days = 0
    currentHeight = 0
    while currentHeight < desiredHeight:
        days = days + 1
        currentHeight = currentHeight + upSpeed
        if currentHeight >= desiredHeight:
            break
        else:
            currentHeight = currentHeight - downSpeed
    print('days:', days)
    return days 