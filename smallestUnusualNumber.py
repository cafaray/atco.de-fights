# Let's call an integer unusual if the sum of its digits is larger than the product of its digits. For example, the numbers 21 and 990 are unusual, while the numbers 22 and 991 aren't.

#Given an integer a (represented as a string), find the smallest unusual integer x such that x ≥ a. Since both x and a can be very large, return the value of x - a.

#Example

#For a = "42", the output should be
#smallestUnusualNumber(a) = 8.

#The smallest unusual number that is greater than or equal to 42 is 50, and 50 - 42 = 8.

# the real one:
def smallest_UnusualNumber(a):
    p = 1
    s = 0
    for x in a:
        p *= int(x)
        s += int(x)
    if s>p:
        return 0
    return 10-int(a[-1])

def smallestUnusualNumber(a):
    w = int(a)    
    while True:
        y,z=0,1
        #print("a =", a)
        for x in range(len(a)):
            y += int(a[x])
            z *= int(a[x])
        #print("y, z", y, z)
        if y>z:
            break
        a = str(int(a) + 1)
        #print(type(a))
    return int(a)-w

a= "42"
expected = 8
print("Assertion case 1", smallestUnusualNumber(a)==expected)

a= "1"
expected = 9
print("Assertion case 2", smallestUnusualNumber(a)==expected)

a = "10"
expected = 0
print("Assertion case 3", smallestUnusualNumber(a)==expected)

a = "11"
expected = 0
print("Assertion case 4", smallestUnusualNumber(a)==expected)

a = "17"
expected = 0
print("Assertion case 5", smallestUnusualNumber(a)==expected)

a = "23"
expected = 7
print("Assertion case 6", smallestUnusualNumber(a)==expected)

a = "1000000000000000000000000000000000000"
expected = 0
print("Assertion case 7", smallestUnusualNumber(a)==expected)

a = "2017"
expected = 0
print("Assertion case 8", smallestUnusualNumber(a)==expected)

a = "8888888888888888888888888888888"
expected = 2
print("Assertion case 9", smallestUnusualNumber(a)==expected)

a = "22"
expected = 8
print("Assertion case 10", smallestUnusualNumber(a)==expected)

a = "21"
expected = 0
print("Assertion case 11", smallestUnusualNumber(a)==expected)
