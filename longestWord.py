import re
def longestWord(text):
    words = text.split()
    maxim = 0
    theWord = ''
    for word in words:
        g = re.search('[a-zA-Z]*', word)
        if len(g.group(0)) > maxim:
            maxim = len(g.group(0))
            theWord = g.group(0)
        print(len(g.group(0)))
    return theWord