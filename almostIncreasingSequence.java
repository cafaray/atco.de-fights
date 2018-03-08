boolean almostIncreasingSequence(int[] sequence) {
    boolean increment = true;
    int removed = -1;
    int last = Integer.MIN_VALUE;
    for(int x=0;x<sequence.length-1;x++){
        if(sequence[x]<sequence[x+1]){
            last = sequence[x];
            increment &= true;
        } else {
            if (removed>-1) return false;
            if(last<sequence[x+1]){
                removed = x;
                last = sequence[x+1];
            } else {
                removed = x + 1;
                last = sequence[x];
            }              
        }
    }
    for(int x=0;x<sequence.length-1;x++){
        if(x==removed){ 
            x++;
        } else if ((x+1)==removed){ 
            if((x+2)<sequence.length){
                increment &= (sequence[x]<sequence[x+2]);
            }
        } else {
            increment &= (sequence[x]<sequence[x+1]);
        }   
    }
    return increment;
}