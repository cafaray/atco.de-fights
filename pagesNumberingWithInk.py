def pagesNumberingWithInk(current, numberOfDigits):    
    s = ''
    while True:
        s += str(current)
        if len(s) >= numberOfDigits: 
            break
        current += 1
    return current if len(s)==numberOfDigits else current - 1