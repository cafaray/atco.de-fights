def calkinWilfSequence(number):
    def fractions():
        tree = ([[1,1]])
<<<<<<< HEAD
        # x,y = 0,-1
        a = b = 1
        while True:
            yield [a, b]
            a, b = b, 2 * (a - a % b) + b - a
            #y+=1
            #yield tree[y]
            #tree += [[tree[x][0],tree[x][0]+tree[x][1]]]
            #y+=1
            #yield tree[y]
            #tree += [[tree[x][0]+tree[x][1],tree[x][1]]]
            #x+=1
=======
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

>>>>>>> 83a07da6c547585075715c4db76f03ce86e66559
    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    print(number, '->', res)
    return res

print("Assertion result on [1,3] = ", calkinWilfSequence([1,3])==3)
print("Assertion result on [14,3] = ", calkinWilfSequence([14,3])==110)
print("Assertion result on [7,13] = ", calkinWilfSequence([7,13])==129)
print("Assertion result on [3,4] = ", calkinWilfSequence([3,4])==13)
print("Assertion result on [4,3] = ", calkinWilfSequence([4,3])==8)
print("Assertion result on [53,37] = ", calkinWilfSequence([53,37])==1080)
print("Assertion result on [37,53] = ", calkinWilfSequence([37,53])==1989)


#mytuple = ("apple", "banana", "cherry")
#myit = iter(mytuple)

#print(next(myit))
#print(next(myit))
#print(next(myit))                                       