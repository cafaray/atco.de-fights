def newNumeralSystem(number):
    num = ord(number)-65
    mynum = num
    res = []
    for x in range(num+1):        
        res+=[chr(x+65) + " + " + chr(mynum+65)]
        mynum -= 1
        if x >= mynum: break
    return res