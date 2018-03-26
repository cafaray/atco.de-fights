def chessBoardCellColor(cell1, cell2):

    c1 = min([ord(cell1[0]), ord(cell2[0])])
    c2 = max([ord(cell1[0]), ord(cell2[0])])
    
    r1 = min([int(cell1[1]), int(cell2[1])])
    r2 = max([int(cell1[1]), int(cell2[1])])
    
    return ((r1+c1)%2 == (r2+c2)%2);