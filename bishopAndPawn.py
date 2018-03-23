def bishopAndPawn(bishop, pawn):
    columnaB = bishop[0]
    #print(ord(columnaB))
    columnaP = pawn[0]
    if columnaB == columnaP: return False
    renglonB = int(bishop[1])
    renglonP = int(pawn[1])
    if renglonB == renglonP: return False
    print('bishop', columnaB + str(renglonB))
    renglonA = renglonB
    columnaA = columnaB
    count = 1
    while columnaA < 'h':            
        caracter = ord(columnaA) + 1
        columnaA = chr(caracter)
        if renglonA - count > 0:
            celda = columnaA + str(renglonA - count)
            print('Celda:', celda)
            if pawn == celda: return True
        if renglonA + count < 9: 
            celda = columnaA + str(renglonA + count)
            print('Celda:', celda)
            if pawn == celda: return True
        count += 1
    
    renglonA = renglonB
    columnaA = columnaB  
    count = 1          
    while columnaA > 'a':            
        caracter = ord(columnaA) - 1
        columnaA = chr(caracter)
        if renglonA - count > 0:
            celda = columnaA + str(renglonA - count)
            print('Celda:', celda)            
            if pawn == celda: return True
        if renglonA < 9: 
            celda = columnaA + str(renglonA + count)
            print('Celda:', celda)     
            if pawn == celda: return True           
        count += 1
    return False