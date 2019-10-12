import re
def longestWord(text):
    a = text.split()
    res = ''
    for x in a:
        n = re.search('[A-Za-z]*', x)        
        if len(res) < len(n.group(0)):
            res = n.group(0) 
    return res