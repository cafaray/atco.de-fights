S=eval(dir()[0])[0]
for i in range(1,len(S)):
    if S[i-1]>=S[i]:
        return False
return True