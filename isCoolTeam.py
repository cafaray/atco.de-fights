class Team(object):
    def __init__(self, names):
        self.names = names

    def createPath(self):
        firsts, lasts = dict(), dict()
        nodes = []
        inout = 0
        for i in self.names:
            il, jl = i[0].lower(), i[-1].lower()
            if il in firsts:
                firsts[il] += [inout]
            else:
                firsts[il] = [inout]
            if jl in lasts:
                lasts[jl] += [inout]
            else:
                lasts[jl] = [inout]
            nodes.append([il, jl])
            inout += 1
        
        # start node
        g,f = 0, 1
        for i in nodes:
            if i[1] in firsts:
                if (i[0] not in lasts) or (len(firsts[i[0]]) > len(lasts[i[0]])):
                    f = 0
                    break
            g += 1
        if f > 0: 
            g = 0  # closed path
        
        visited = [0]*len(nodes)
        trace = firsts[nodes[g][0]]
        while trace != []:
            i = trace.pop(0)
            visited[i] = 1
            try : 
                l = firsts[nodes[i][1]][:]
                for j in l:
                    if visited[j] == 0 :
                        trace.append( firsts[ nodes[i][1] ].pop(0)  )
            except: 
                pass
        return visited

    def __bool__(self):        
        f = [i[0].lower() for i in self.names]
        l = [i[-1].lower() for i in self.names]
        for i in f :
            try:
                l.remove(i)
            except:
                pass
        if len(l) > 1:
            return False    

        # if base condition does not satisfied the result, so, validate through eulier path
        visited = self.createPath()
        # check eulier path, where all nodes are visited almost once time          
        for i in visited:
            if i == 0 : return False
        return True

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
