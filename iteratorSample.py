def calkinWilfSequence(number):
    def fractions():
        tree = ([[1,1]])
        x,y = 0,0
        while True:
            yield tree[y]
            tree += [[tree[x][0],tree[x][0]+tree[x][1]]]
            y+=1
            yield tree[y]
            tree += [[tree[x][0]+tree[x][1],tree[x][1]]]
            y+=1
            x+=1


        #a, b = b, 2 * (a - a % b) + b - a

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res


print("Assertion result on [1,3] = ", calkinWilfSequence([1,3])==3)
print("Assertion result on [14,3] = ", calkinWilfSequence([14,3])==110)
print("Assertion result on [7,13] = ", calkinWilfSequence([7,13])==129)

#mytuple = ("apple", "banana", "cherry")
#myit = iter(mytuple)

#print(next(myit))
#print(next(myit))
#print(next(myit))