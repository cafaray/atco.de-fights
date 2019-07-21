def isSmooth(arr):
        midl = arr[len(arr)//2-1] + arr[len(arr)//2] if len(arr)%2 == 0 else arr[len(arr)//2]    
        return True if midl == arr[0] and midl == arr[-1] else False