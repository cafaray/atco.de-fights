class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def reverseNodesInKGroups(l, k):
    res=[]
    x=0
    while l:
        c = []
        while x<k:
            if l:
                v = l.value        
                l = l.next                
                c+= [v]
                x+=1
            else:
                res+=c[:]
                return res
        x=0
        res+=c[::-1]
    return res

