def isCryptSolution(crypt, solution):
    d={}
    for s in solution:
        d[s[0]]=s[1]
    n=[]
    for w in range(len(crypt)):
        s=''
        for c in range(len(crypt[w])):
            s+=d[crypt[w][c]]
            if len(s)>1 and s[0]=='0': return Falses
        n+=[s]
    return int(n[0]) + int(n[1]) == int(n[2]) 

crypt = ["SEND", "MORE", "MONEY"]
solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]

print("Assertion: ", isCryptSolution(crypt, solution)==True)

crypt = ["TEN", "TWO", "ONE"]
solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]

print("Assertion: ", isCryptSolution(crypt, solution)==False)
