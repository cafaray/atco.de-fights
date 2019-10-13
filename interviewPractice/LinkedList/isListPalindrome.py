# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def isListPalindrome(l):
    a=[]
    while l is not None:
        #print(l.value)
        a+=[l.value]
        l=l.next
    return a==a[::-1]