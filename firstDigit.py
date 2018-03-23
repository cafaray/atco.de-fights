def firstDigit(inputString):
    for element in inputString:
        try:
            number = int(element)
            break
        except:
            continue
    return element