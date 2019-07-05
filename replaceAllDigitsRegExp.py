def replaceAllDigitsRegExp(input):
    r = ''
    ready = False
    for c in input:
        if c>='0' and c<='9' and not ready:
            r+='#'
            ready = True
        else:
            r+=c
    return r

def replaceAllDigitsRegExp1(input):
    r=''
    for x in input:
        if '0' <= x <= '9':
            r+='#'
        else:
            r+=x
    return r