def directionOfReading(numbers):
    for i in range(len(numbers)):
        numbers[i] = ["0"*100 + str(numbers[i])][0][-len(numbers):]
    print numbers
    out = ["" for i in range(len(numbers))]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            out[j] += numbers[i][j]
    print out
    return map(int,out)
