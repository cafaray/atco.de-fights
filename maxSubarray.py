def maxSubarray(matrix):
    res = 0    
    for i in range(len(matrix)):        
        cur = 0
        for j in range(i, len(matrix)):         
            cur += matrix[j]
            if res < cur:
                res = cur
    return res