def replaceAllDigitsRegExp(input):
    r = ''
    for c in input:
        if c >= '0' and c<= '9':
            r += '#'
        else:
            r+=c
    return r