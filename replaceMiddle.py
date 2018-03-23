def replaceMiddle(arr):
     
    if len(arr)%2 == 0:
        midl = arr[len(arr)//2-1] + arr[len(arr)//2] if len(arr)%2 == 0 else arr[len(arr)//2]
        arr = arr[:len(arr)//2-1]+[midl]+arr[len(arr)//2+1:]               
    return arr 