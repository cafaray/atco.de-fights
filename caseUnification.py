def caseUnification(inputString):
    low = [x for x in inputString if x>='a' and x<='z']
    if len(low) > len(inputString) - len(low):
        return inputString.lower()
    else:
        return inputString.upper()