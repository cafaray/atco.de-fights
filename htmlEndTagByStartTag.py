def htmlEndTagByStartTag(startTag):    
    elem = startTag.split(" ")[0][1:]    
    return  "</" + elem + (">" if elem[-1]!=">" else "")    




print(htmlEndTagByStartTag("<div sometrash>"))