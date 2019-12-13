S=sorted(eval(dir()[0])[0])
for x in range(1,len(S)):
    if S[x-1]==S[x]:
        return True
return False