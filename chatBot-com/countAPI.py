def countAPI(calls):    
    marked = []
    res = []
    for x in range(len(calls)):     
        px = calls[x].split('/')           
        domain = 0            
        for p in calls:
            pz = p.split('/')                
            if pz[1] == px[1]:
                domain += 1
        if px[1] +' ('+str(domain)+')' not in marked:
            marked+=[px[1]+' ('+str(domain)+')']
    
    for x in marked:
        res += ['--' + x]
        p = x[:x.find(' (')]
        contexts = findContext(p, calls)        
        for y in contexts:
            res += ['----'+y]
            s = y[:y.find(' (')]
            methods = findMethods(p+'/'+s, calls)
            for t in methods:
                res += ['------' + t]
            
    return res
    
def findMethods(context, calls):
    temp = []
    for x in calls:
        sx = x.split('/')        
        if context != sx[1]+'/'+sx[2]:
            continue
        m = 0
        for z in calls:
            sz = z.split('/')
            if sx[1]+sx[2]+sx[3] == sz[1]+sz[2]+sz[3]:
                m += 1
        if m > 0 and context == sx[1]+'/'+sx[2] and sx[3] + ' ('+str(m)+')' not in temp:
            temp += [sx[3] + ' (' + str(m) + ')']
    return temp
    
def findContext(project, calls):    
    temp = []
    for x in calls:
        sx = x.split('/')
        if project != sx[1]:
            continue
        c = 0    
        for z in calls:
            sz = z.split('/')
            if sx[1]+sx[2] == sz[1]+sz[2]:
                c += 1
        if  c>0 and project == sx[1] and sx[2] + ' ('+str(c)+')' not in temp:
            temp += [sx[2] + ' (' + str(c) + ')']
    return temp
