def buscaIteraciones(fileName, names):
    cuenta = 1
    print('---> buscando iteraciones de:', fileName, ' in', names)        
    while True:
        if fileName + '(' + str(cuenta) + ')' in names:
            cuenta+=1
        else:
            return cuenta    

def fileNaming(names):
    files = list()
    for name in names:
        if name in files:
            #print(name[:len(name)], ':', name[len(name):])
            iteraciones = buscaIteraciones(name, files)
            if iteraciones == 0: iteraciones = 1
#            print('busca iteraciones: ', iteraciones)
            files.append(name + '(' + str(iteraciones) + ')')
        else:
            files.append(name)
        
#        print(files)
    return files