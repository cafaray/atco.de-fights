import arrayMaxConsecutiveSum
def arrayMaxConsecutiveSum(inputArray, k):
    #maxn = 0

    #for element in range(len(inputArray) - k + 1):
    #    suma = sum(inputArray[element:element+k])
    #    if maxn < suma: maxn = suma
    #return maxn

    result = 0
    currentSum = 0

    for i in range(0,k):
        currentSum += inputArray[i]

    for i in range(k-1,len(inputArray)):
        currentSum += inputArray[i]
        if currentSum > result:
            result =  currentSum
        currentSum -= inputArray[i - k + 1]
    return result


print(arrayMaxConsecutiveSum())
  #for (int i = 0; i < k - 1; i++) {
  #  currentSum += inputArray[i];
  #}
  # for (int i = k - 1; i < inputArray.length; i++) {
  #  currentSum += inputArray[i];
  #  if (currentSum > result) {
  #    result =  currentSum ;
  #  }
  #  currentSum -= inputArray[i - k + 1];
  # }

  #return result;