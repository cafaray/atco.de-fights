def firstDuplicate(a):
    s=set()
    for i in range(len(a)):
        if a[i] in s:    
            return a[i]
        s.add(a[i])
    return -1
# --------------------------------------------------------- #
# Alternative solution that doesn't work time exceded:    - #
# a=eval(dir()[0])[0]                                     - #
# for i in range(1,len(a)):                               - #
#     if a[i] in a[:i]:                                   - #
#         return a[i]                                     - #
# return -1                                               - #
# --------------------------------------------------------- #

a= [2, 1, 3, 5, 3, 2]
print(firstDuplicate(a))