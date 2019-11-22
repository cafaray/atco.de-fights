def isDivisibleBy6(inputString):
    
    digitSum = 0
    leftBound = ord('0')
    rightBound = ord('9')
    answer = []
    mask = list(inputString)
    asteriskPos = -1

    for i in range(len(mask)):
        if (leftBound <= ord(mask[i]) and
          ord(mask[i]) <= rightBound):
            digitSum += ord(mask[i]) - leftBound
        else:
            asteriskPos = i

    for i in range(10):
        if (digitSum + i) % 3 == 0:
            mask[asteriskPos] = chr(leftBound + i)
            if (ord(mask[len(mask) - 1]) - leftBound) % 2 == 0:
                answer.append(''.join(mask))

    return answer


def isDivisibleBy6(inputString):
    r=[]
    for i in range(0,10):
        n=int(inputString.replace("*", str(i)))
        if n%6==0:
            r+=[str(n)]
    return r