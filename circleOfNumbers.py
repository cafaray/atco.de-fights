def circleOfNumbers(n, firstNumber):
    mid = n // 2
    if firstNumber >= mid: return firstNumber - mid
    return mid + firstNumber
