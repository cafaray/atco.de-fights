def createList(calls):
    metodos = 0
    for y in calls:
        if y == calls[x]:
            metodos += 1
            marked[x][2] = metodos
    context = 0            
    for y in calls:
        py = y.split('/')                
        if py[1] == px[1] and py[2] == px[2]:
            context += 1
            marked[x][1] = metodos
    
    calls = sorted(calls)
    lc = ''
    resPro = {}
    cp = 0
    for c in calls:
        pr = c[1:c.find('/',1)]
        if lc != pr:            
            cp = 0
            sp = [s[len(pr)+2:s.find('/', len(pr)+3)] for s in calls if '/'+pr+'/' in s]
            sp = sorted(sp)
            ls = ''    
            resSub = {}
            cs = 0
            for x in sp:
                if ls != x: 
                    mt = [m[len(pr+x)+3:] for m in calls if '/'+pr+'/'+x+'/' in m]
                    mt = sorted(mt)
                    lm = ''  
                    cm = 0
                    cs = 0
                    res = []
                    for y in mt:
                        if lm != y:
                            cm = 0
                            res += ['------'+y+' (1)']
                            lm = y
                        cm += 1
                        cs += 1
                        cp += 1
                        res[-1] = res[-1].replace(' ('+str(cm-1)+')', ' ('+str(cm)+')') 
                    ls = x
                    resSub['----'+x+' ('+str(cs)+')'] = res
            resPro['--'+pr+' ('+str(cp)+')'] = resSub
            lc = pr
    r = []
    for k,v in resPro.items():        
        r += [k]
        for sk, sv in v.items():
            r += [sk]
            for mv in sv:
                r+=[mv]
    return r