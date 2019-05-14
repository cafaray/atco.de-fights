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