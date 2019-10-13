# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    r=[]
    while l1 or l2:
        if l1:
            r+=[l1.value]
            l1 = l1.next            
        if l2:
            r+=[l2.value]
            l2=l2.next                    
    return sorted(r)