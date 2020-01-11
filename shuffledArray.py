def shuffledArray(shuffled):
    s=0
    m=max(shuffled)
    for i in range(len(shuffled)):
        s=0
        for j in range(len(shuffled)):
            if i==j: continue
            s+=shuffled[j]
        if s==shuffled[i]:
            shuffled.remove(s)
            return sorted(shuffled)


shuffled= [1, 12, 3, 6, 2]
e=[1, 2, 3, 6]
#r=shuffledArray(shuffled)
#print("Assertion for test 1:", e==r)

shuffled= [2, -1, 2, 2, -1]
e=[-1, -1, 2, 2]
r=shuffledArray(shuffled)
print("Assertion for test 3:", e==r)

shuffled= [-3, -3]
e=[-3]
r=shuffledArray(shuffled)
print("Assertion for test 4:", e==r)