class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        firsts=[x[0].lower() for x in self.names]
        lasts=[x[-1].lower() for x in self.names]
        for x in firsts:
            try:
                lasts.remove(x)
            except:
                pass
        return len(lasts)==1

def isCoolTeam(team):
    return bool(Team(team))

team=["Mark", 
 "Kelly", 
 "Kurt", 
 "Terk"]
expected=True
print("Assertion result for test case 1 is:", isCoolTeam(team)==expected)

team=["Lucy"]
expected=True
print("Assertion result for test case 2 is:", isCoolTeam(team)==expected)

team=["Rob", 
 "Bobby", 
 "Billy"]
expected=False
print("Assertion result for test case 3 is:", isCoolTeam(team)==expected)

team=["Sophie", 
 "Boris", 
 "EriC", 
 "Charlotte"]
expected=True
print("Assertion result for test case 4 is:", isCoolTeam(team)==expected)

team=["Ron", 
 "Harry"]
expected=False
print("Assertion result for test case 5 is:", isCoolTeam(team)==expected)

team=["Alice", 
 "Ewan", 
 "Nick", 
 "Kaa", 
 "Mary", 
 "Yram"]
expected=False
print("Assertion result for test case 6 is:", isCoolTeam(team)==expected)

team=["Alice", 
 "Evan", 
 "Natasha", 
 "Kaa", 
 "Mary", 
 "Yram", 
 "Ak"]
expected=False
print("Assertion result for test case 7 is:", isCoolTeam(team)==expected)

team=["Lah", 
 "Leh", 
 "Luh", 
 "Hel"]
expected=False
print("Assertion result for test case 8 is:", isCoolTeam(team)==expected)

team=["Sophie", 
 "Boris", 
 "Eric", 
 "Charlotte", 
 "Charlie"]
expected=False
print("Assertion result for test case 9 is:", isCoolTeam(team)==expected)

team=["Sophie", 
 "Edward", 
 "Deb", 
 "Boris", 
 "Stephanie", 
 "Eric", 
 "Charlotte", 
 "Eric", 
 "Charlie"]
expected=True
print("Assertion result for test case 10 is:", isCoolTeam(team)==expected)

team=["Caleb", 
 "Dale", 
 "Edward"]
expected=False
print("Assertion result for test case 11 is:", isCoolTeam(team)==expected)

team=["Bobo", 
 "obob", 
 "Bobo", 
 "ob"]
expected=True
print("Assertion result for test case 12 is:", isCoolTeam(team)==expected)

team=["Edward", 
 "Daniel", 
 "Lily"]
expected=True
print("Assertion result for test case 13 is:", isCoolTeam(team)==expected)

team=["ANTONY", 
 "James"]
expected=False
print("Assertion result for test case 14 is:", isCoolTeam(team)==expected)

team=["Ned", 
 "Ben"]
expected=True
print("Assertion result for test case 15 is:", isCoolTeam(team)==expected)

team=["sadasdassad", 
 "asdssw"]
expected=False
print("Assertion result for test case 16 is:", isCoolTeam(team)==expected)
