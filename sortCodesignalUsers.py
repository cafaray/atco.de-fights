def sortCodesignalUsers(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))


class CodeSignalUser:
        
    #def mycmp(o1, o2):
        #return o1[2]-o2[2]
        
    def __gt__(self, other):
        if self.xp>other.xp:
            return self
        elif self.xp<other.xp:
            return other
        else:
            if self.id < other.id:
                return self
            else:
                return other
    
    def __lt__(self, other):
        if self.xp<other.xp:
            return self
        elif self.xp>other.xp:
            return other
        else:
            if self.id < other.id:
                return self
            else:
                return other

    def __eq__(self, other):
        if self.xp==other.xp:
            if self.id < other.id:
                return self
            else:
                return other

    def __str__(self):
        return self.level

    def __init__(self, level, id, xp):
        self.level = level
        self.id = id
        self.xp = xp

users = [["warrior", "1", "1050"],
         ["Ninja!",  "21", "995"],
         ["recruit", "3", "995"]]
print(sortCodesignalUsers(users))