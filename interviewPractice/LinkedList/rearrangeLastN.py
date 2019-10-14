# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):    
    reverse=reverse_list(l)    
    c=0
    res=[]
    while True:
        if c<n:
            c+=1
            res+=[reverse.value]
            reverse=reverse.next
            continue
        res=res[::-1]
        break        
    tmp=[]
    while reverse:
        tmp+=[reverse.value]
        reverse=reverse.next
    res+=tmp[::-1]        
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