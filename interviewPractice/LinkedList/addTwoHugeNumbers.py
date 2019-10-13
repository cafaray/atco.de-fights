def addTwoHugeNumbers(a, b):
    a = reverse_list(a)
    b = reverse_list(b)    
    res = []
    keep=0    
    while a or b:
        val=0
        if a:
            val+=a.value
            a=a.next
        if b:
            val+=b.value
            b=b.next
        keep,val=divmod(val+keep,10000)
        res.insert(0, val)
    if keep>0: res.insert(0,keep)
    return res

def reverse_list(theList):
    current = theList
    parent = None
    tempChild = None
    while current:
        tempChild = current.next
        current.next = parent
        parent = current
        current = tempChild
    return parent


a= [1]
b= [9998, 9999, 9999, 9999, 9999, 9999]
res = addTwoHugeNumbers(a, b)
print(res, "Assertion:", res==[9999, 0, 0, 0, 0, 0])


    