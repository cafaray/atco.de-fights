def firstReverseTry(arr):
    return arr if  len(arr) == 1 else arr[len(arr)-1:] + arr[1:len(arr)-1] + arr[:1]
