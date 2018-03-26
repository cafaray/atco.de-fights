def addBorder(picture):
    nuevo = []
    for x in range(len(picture)+2):
        nuevo+=['']

    lg = len(picture[0])+2
    p = 1
    for c in picture:        
        nuevo[p] = '*' + c + '*'
        p+=1

    nuevo[0] = ''
    for x in range(lg):
        nuevo[0] += '*'

    nuevo[len(nuevo)-1] = nuevo[0]
    return nuevo