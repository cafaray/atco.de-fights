# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    r=[]
    while l is not None:
        if l.value!=k:
            r+=[l.value]
        l = l.next
    return r