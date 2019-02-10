def splitByValue(k, elements):
    lt=[]
    gt=[]
    for i in range(len(elements)):
        if elements[i]<k:
            lt+=[elements[i]]
            continue
        else:
            gt+=[elements[i]]

    print(lt+gt)
elements=[1, 3, 5, 7, 6, 4, 2]
print(splitByValue(5, elements))