def overlappingFindAndReplace(text, pattern, replacement):
    n,l,r=list(text),len(pattern),len(replacement)    
    for x in range(len(text)):        
        if text[x:x+l]==pattern:n[x:x+r]=replacement
    return ''.join(n)


    n=list(text)
    for x in range(len(text)):
        if text[x:x+len(pattern)]==pattern:n[x:x+len(replacement)]=replacement
    return ''.join(n)
