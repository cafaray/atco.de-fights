def validTime(time):
    arrTime = time.split(':')
    hours = arrTime[0]
    minutes = arrTime[1]
    try:
        iHours = int(hours)
        iMinutes = int(minutes)
    except:
        print('hours:',hours, '    minutes:',minutes)
        return False
    if iHours >= 0 and iHours < 24:
        if iMinutes >= 0 and iMinutes < 60:
            return True
    return False