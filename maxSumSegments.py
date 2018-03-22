def maxSumSegments(a):

    res = [0 for i in range(len(a))]
    for i in range(1,len(a)+1):
        s=0
        mx=0
        index=-1
        for j in range(len(a)):
            s+=a[j]
            if j>=i:
                s-=a[j-i]
            if j>=i-1 and( index==-1 or s>mx):
                mx=s
                index=j-i+1
        res[i-1]=index
    return res