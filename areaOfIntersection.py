def areaOfIntersection(shape1, shape2):
    cells = 0
    for x in range(shape1[1]-shape1[0], shape[1]+shape[0]):
        for y in range(shape1[2] - shape1[0], shape[2]+shape[0]):
            diff1 = abs(x - shape1[1]) + abs(y - shape1[2])
            diff2 = abs(x - shape2[1]) + abs(y - shape2[2])
            if diff1 < shape1[0] and diff2 < shape2[0]: cells+=1 
    return cells
    
    #areaOfIntersection([r1, x1, y1], [r2, x2, y2]) {
    #let cells = 0;
    
    #for(let x = x1 - r1; x <= x1 + r1; x++) {
    #    for(let y = y1 - r1; y <= y1 + r1; y++) {
    #        const diff1 = Math.abs(x - x1) + Math.abs(y - y1);
    #        const diff2 = Math.abs(x - x2) + Math.abs(y - y2);
    #        if(diff1 < r1 && diff2 < r2) cells++;
    #    }
    #}
    
    #return cells;