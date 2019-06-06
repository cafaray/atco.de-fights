def isEarlier(time1, time2):
    if time1[0]<time2[0]:
        return True
    if time1[0]==time2[0]:
        if time1[1]<time2[1]:
            return True
    return False    