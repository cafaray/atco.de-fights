def replaceFirstDigitRegExp(input):
    res = ''
    ready = False
    for x in input:
        if x.isdigit():
            res += '#'
        else:
            res += x
        print(res)
    return res