def extractFees(infadi):
    feesDefaultLength = 15
    startPosition = 24
    values = []
    for x in range(startPosition, 215, feesDefaultLength):
        try:
            values+=[int(infadi[x:x+feesDefaultLength])/100]
        except:
            print("some no decimal value")
        print(x)
    x+=feesDefaultLength
    print(x)
    currency = infadi[x:x+3]
    values += [currency]
    return values

print(extractFees("                     12A000000000000000000000000000000999999999999999000000000000000000000000000000000000000000000000000000000000000000000000095000000000000095000000000000000000000000000000000000000000000000000000000095EUR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       client_tppC"))