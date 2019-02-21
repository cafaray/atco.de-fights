def calkinWilfSequence(number):
    def fractions():
        last = ([1,1],[1,1])
        r = True
        while True:
            #print('before yield', last, r)
            yield last[1 if r else 0]
            if r:
                last = [[last[0][0], last[0][0]+last[0][1]], [last[1][0], last[1][1]]] 
            else:
                last = [[last[0][0], last[0][1]], [last[1][0]+last[1][1], last[1][0]]]       
            r = not r
            #print('after yield')

    gen = fractions()
    res = 0
    while True:
        n = next(gen)
        print(n)
        if n == number:
            break
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