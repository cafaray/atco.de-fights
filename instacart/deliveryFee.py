def deliveryFee(intervals, fees, deliveries):
    if len(intervals)==1: return True
    di = {}
    for deliver in deliveries:
        findInterval = False
        for interval in range(len(intervals)-1):
            if intervals[interval] <= deliver[0] < intervals[interval+1]:
                di[intervals[interval]] = di.get(intervals[interval], 0) + 1
                findInterval=True
        if not findInterval: di[intervals[-1]] = di.get(intervals[-1], 0) + 1
    #print(di, len(di))
    if len(di)!=len(fees): return False
    intervalFees = 0
    for k in range(len(di)):        
        print('fees[k]/di[intervals[k]] =', fees[k], '/',di[intervals[k]], fees[k]//di[intervals[k]])
        if intervalFees==0:
            print('intervalFees = ', fees[k]/di[intervals[k]])
            intervalFees = fees[k]/di[intervals[k]]
        if fees[k]/di[intervals[k]]!=intervalFees:
            return False
    return True


intervals= [0, 10, 22]
fees= [1, 3, 1]
deliveries= [[8,15], 
 [12,21], 
 [15,48], 
 [20,17], 
 [23,43]]
expected=True
print("Assertion for excercise 1, ", deliveryFee(intervals, fees, deliveries)==expected)

intervals= [0, 10, 22]
fees= [1, 3, 1]
deliveries= [[8,15], 
 [12,21], 
 [15,48], 
 [20,17]]
expected=False
print("Assertion for excercise 2, ", deliveryFee(intervals, fees, deliveries)==expected)

intervals= [0, 22]
fees= [1, 1]
deliveries= [[5,34], 
 [21,23], 
 [23,0], 
 [23,1], 
 [23,59]]
expected=False
print("Assertion for excercise 3, ", deliveryFee(intervals, fees, deliveries)==expected)

intervals= [0]
fees= [34343]
deliveries= [[12,34], 
 [14,45], 
 [17,58], 
 [23,25]]
expected=True
print("Assertion for excercise 4, ", deliveryFee(intervals, fees, deliveries)==expected)

intervals= [0, 10, 23]
fees= [3, 3, 3]
deliveries= [[0,12], 
 [0,13], 
 [0,51], 
 [9,17], 
 [10,3], 
 [10,59], 
 [22,22], 
 [22,23], 
 [23,0], 
 [23,17], 
 [23,47], 
 [23,48]]
expected=True
print("Assertion for excercise 5, ", deliveryFee(intervals, fees, deliveries)==expected)

intervals= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
fees= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
deliveries= [[0,32], 
 [1,58], 
 [2,10], 
 [3,23], 
 [4,59], 
 [5,4], 
 [6,36], 
 [7,52], 
 [8,38], 
 [9,7], 
 [10,43], 
 [11,54], 
 [12,7], 
 [13,15], 
 [14,12], 
 [15,29], 
 [16,48], 
 [17,1], 
 [18,47], 
 [19,21], 
 [20,13], 
 [21,51], 
 [22,7], 
 [23,20]]
expected=False
print("Assertion for excercise 6, ", deliveryFee(intervals, fees, deliveries)==expected)

intervals= [0]
fees= [100000]
deliveries= [[1,35]]
expected=True
print("Assertion for excercise 7, ", deliveryFee(intervals, fees, deliveries)==expected)

intervals= [0, 15]
fees= [100000, 100000]
deliveries= [[1,35], 
 [15,0]]
expected=True
print("Assertion for excercise 8, ", deliveryFee(intervals, fees, deliveries)==expected)

intervals= [0, 15]
fees= [100000, 99999]
deliveries= [[1,35], 
 [15,0]]
expected=False
print("Assertion for excercise 9, ", deliveryFee(intervals, fees, deliveries)==expected)

intervals= [0, 4, 13]
fees= [2, 3, 2]
deliveries= [[1,35], 
 [2,15], 
 [4,1], 
 [5,37], 
 [7,55], 
 [13,46], 
 [17,9]]
expected= True
print("Assertion for excercise 10, ", deliveryFee(intervals, fees, deliveries)==expected)