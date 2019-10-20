def longestUncorruptedSegment_orig(sourceArray, destinationArray):
#    a = zip(sourceArray,destinationArray )
#    for i, e in enumerate(a):
#        if e[0] == e[1]:
#            res.append(0)
#        else:
#            res.append(1)    
    # d = differences
    d=[sourceArray[x]!=destinationArray[x] for x in range(len(sourceArray))]
    # len, start, n = segments, i= start pos, p = previous is diff
    l,s,n,i,p = 0,0,0,0,False
    for x in range(len(d)):
        if d[x]:
            n=0    # start the n segments 
        else:
            n+=1   # count segments from previous difference
            if x==0 or p:    # is first or previous difference
                i=x          # so, start must be rewrite
            if l<n:          # is there some segments previosly counted
                l,s=n,i      # set new segments count and new start position
        p=d[x]               # set previous result diference evaluation
    return [l,s]

sourceArray=[33531593, 96933415, 28506400, 39457872, 29684716, 86010806]
destinationArray=[33531593, 96913415, 28506400, 39457872, 29684716, 86010806]
expected=[4, 2]
response = longestUncorruptedSegment(sourceArray, destinationArray)
print("Assertion: ", response,"=",expected, ": ", response==expected)

sourceArray= [10000000]
destinationArray= [99999999]
expected=[0, 0]
response = longestUncorruptedSegment(sourceArray, destinationArray)
print("Assertion: ", response,"=",expected, ": ", response==expected)

sourceArray= [20800440, 98256958, 64277103, 40475664, 98589505, 31621824, 84322264, 58283379, 15631261, 35464021]
destinationArray= [20800440, 95256958, 64276103, 40475664, 98589505, 31621824, 84322264, 58283379, 15631261, 35464021]
expected=[7, 3]
response = longestUncorruptedSegment(sourceArray, destinationArray)
print("Assertion: ", response,"=",expected, ": ", response==expected)


sourceArray=[28813641, 31985183, 49809398, 48959083, 59368847, 37296474, 92567090, 50320165, 12197477, 28906340]
destinationArray=[38813641, 31983183, 49879398, 48959043, 59468847, 35296474, 92567020, 80320165, 14197477, 28906360]
expected = [0,0]

sourceArray=[92988800, 80253955, 17396563, 91682092, 77708269, 97587946, 23889892, 20661856, 21013095, 92028000, 17562863, 86804822, 17819093, 97941923, 64955308]
destinationArray=[92988800, 80253955, 17396563, 91682092, 77708229, 97587946, 23889892, 20661866, 21013095, 92928000, 17962863, 86804822, 14819093, 97241923, 62955308]
expected = [4,0]

sourceArray=[99919628, 77504204, 18846830, 86785029, 86230362, 96953294, 53208680, 95327090, 68996760, 26366538, 90490275, 62583792, 87514087, 96921389, 21309822]
destinationArray=[99919628, 77503204, 18546830, 86785029, 86230362, 96953264, 53208680, 95327090, 68996760, 26366538, 90420275, 62583792, 87514087, 39692139, 21303822]
expected = [4,6]

