'''
When migrating data from a source storage system to a target storage system, 
the number one focus is avoiding data corruption at all cost. 

In order to meet these high standards, various rounds of tests are run checking 
for corrupted blocks as well as successfully migrated lengthy regions.

We are going to represent the source storage system and target storage system 
as sequential arrays sourceArray and destinationArray respectively, where sourceArray[i] 
represents binary data of the ith source block as an integer, and destinationArray[i] 
represents binary data of the ith destination block, where the data should be migrated, 
also as an integer. 

Given the content of the source and the migrated content of the target, find the length 
and the starting block of the longest uncorrupted data segment (segment = subsequent blocks).

If there is no uncorrupted segment, return an array containing 0 and 0 respectively.
'''

def longestUncorruptedSegment(sourceArray, destinationArray):
    s,p=0,-1
    r=[]
    for x in range(len(sourceArray)):
        if sourceArray[x]==destinationArray[x]:
            if p<0: p=x
            s+=1            
        else:
            if s>0: r+=[(s,p)]
            s,p=0,-1 
    if s>0: r+=[(s,p)]
    r=sorted(r)
    return [0,0] if len(r)<=0 else [r[-1],len(sourceArray)-r[-1]]


sourceArray=     [33531593, 96933415, 28506400, 39457872, 29684716, 86010806]
destinationArray=[33531593, 96913415, 28506400, 39457872, 29684716, 86010806]
r=longestUncorruptedSegment(sourceArray, destinationArray)
print("Assertion gaven: ", r==[4, 2], " Result is:", r)

sourceArray=     [10000000]
destinationArray=[99999999]
r=longestUncorruptedSegment(sourceArray, destinationArray)
print("Assertion gaven: ", r==[0, 0], " Result is:", r)

sourceArray=     [20800440, 98256958, 64277103, 40475664, 98589505, 31621824, 84322264, 58283379, 15631261, 35464021]
destinationArray=[20800440, 95256958, 64276103, 40475664, 98589505, 31621824, 84322264, 58283379, 15631261, 35464021]
r=longestUncorruptedSegment(sourceArray, destinationArray)
print("Assertion gaven: ", r==[7, 3], " Result is:", r)

sourceArray=     [28813641, 31985183, 49809398, 48959083, 59368847, 37296474, 92567090, 50320165, 12197477, 28906340]
destinationArray=[38813641, 31983183, 49879398, 48959043, 59468847, 35296474, 92567020, 80320165, 14197477, 28906360]
r=longestUncorruptedSegment(sourceArray, destinationArray)
print("Assertion gaven: ", r==[0, 0], " Result is:", r)

sourceArray=     [92988800, 80253955, 17396563, 91682092, 77708269, 97587946, 23889892, 20661856, 21013095, 92028000, 17562863, 86804822, 17819093, 97941923, 64955308]
destinationArray=[92988800, 80253955, 17396563, 91682092, 77708229, 97587946, 23889892, 20661866, 21013095, 92928000, 17962863, 86804822, 14819093, 97241923, 62955308]
r=longestUncorruptedSegment(sourceArray, destinationArray)
print("Assertion gaven: ", r==[4, 0], " Result is:", r)

sourceArray=[99919628, 77504204, 18846830, 86785029, 86230362, 96953294, 53208680, 95327090, 68996760, 26366538, 90490275, 62583792, 87514087, 96921389, 21309822]
destinationArray=[99919628, 77503204, 18546830, 86785029, 86230362, 96953264, 53208680, 95327090, 68996760, 26366538, 90420275, 62583792, 87514087, 39692139, 21303822]
r=longestUncorruptedSegment(sourceArray, destinationArray)
print("Assertion gaven: ", r==[4, 6], " Result is:", r)
