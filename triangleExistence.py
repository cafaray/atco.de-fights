def triangleExistence(sides):
    s=sorted(sides)
    return s[0]+s[1]>s[2]