import re
s=eval(dir()[0])[0][::-1]
return s[re.search(r'\d+',s).start()]

s,i=eval(dir()[0])[0],-1
while not('0'<=s[i]<='9'): i-=1
return s[i]