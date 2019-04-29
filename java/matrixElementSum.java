int matrixElementsSum(int[][] matrix) {

    Integer[] suspended = new Integer[matrix[0].length];
    int suma = 0;
    for(int i=0;i<matrix.length;i++){
        for(int j = 0;j < matrix[i].length; j++){
            
            suma += isSuspended(suspended, j)?0:matrix[i][j];

            if(matrix[i][j]==0){
                for(int z = 0; z < suspended.length ; z++){
                    if(suspended[z]==null){
                        suspended[z] = j;
                        break;
                    }
                }
            }
        }
    }
    return suma;
}

boolean isSuspended(Integer[] suspended, int col){
    for(int x = 0; x < suspended.length; x++){
        if(suspended[x]==null) return false;
        if(suspended[x]== col) return true;
    }
    return false;
}
