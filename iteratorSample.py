def calkinWilfSequence(number):
    def fractions():
        last = (1, 1)
        while True:
            yield last
            last = last[0], last[1] + last[0]

    gen = fractions()
    print(gen)
    res = 0
    while next(gen) != number:
        res += 1
    return res


print(calkinWilfSequence([1,3]))

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))