def splitString(str):
    slicedArray = re.findall('\\w+\\s', str + " ")
    for i in range(len(slicedArray)):
        slicedArray[i] = slicedArray[i].strip() 
    return slicedArray