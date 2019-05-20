def shoppingList(items):
    item = ''
    realItems = []
    startNumber = False
    for c in items:
        if '0'<=c<='9':            
            startNumber = True
            item+=c 
        elif c=='.' and startNumber:
            item+=c 
        else:
            if startNumber:
                print(item)
                realItems.append(float(item))
                item = ''
                startNumber = False
            continue
    if len(item)>0: realItems.append(float(item))
    return(sum(realItems))