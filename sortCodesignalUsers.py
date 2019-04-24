from functools import total_ordering
def sortCodesignalUsers(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))

@total_ordering
class CodeSignalUser:

    def __eq__(self, other):
        return (self.xp == other.xp)

    def __ne__(self, other):
        return not (self==other)    

    #def __repr__(self):
    #    return "%s %s" % (self.first, self.last)

    def __lt__(self, other):
        if self.xp < other.xp:
            return True
        elif self.xp == other.xp:
            if self.id > other.id:
                return True            
        return False
        
    def __gt__(self, other):
        if self.xp > other.xp:
            return True
        elif self.xp == other.xp:
            if self.id < other.id:
                return True            
        return False
    
    def __ge__(self, other):
        if self.xp >= other.xp:
            return True
        elif self.xp >= other.xp:
            if self.id < other.id:
                return True            
        return False
    
    def __le__(self, other):
        if self.xp <= other.xp:
            return True
        elif self.xp <= other.xp:
            if self.id < other.id:
                return True            
        return False

    def __str__(self):
        return self.level

    def __init__(self, level, id, xp):
        self.level = level
        self.id = int(id)
        self.xp = int(xp)

users = [["warrior", "1", "1050"],
         ["Ninja!",  "21", "995"],
         ["recruit", "3", "995"],
         ["recruit2", "31", "1993"]]
print(sortCodesignalUsers(users))