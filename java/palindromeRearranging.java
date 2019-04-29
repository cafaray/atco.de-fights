boolean palindromeRearranging(String inputString) {
    if(inputString.length()==1)return true;
    char[] arreglo = inputString.toCharArray();
    Arrays.sort(arreglo);
    if(inputString.length()%2!=0){
        boolean unaDiferente = false;
        for(int x=0;x<arreglo.length-1;x++){
            if(arreglo[x]!=arreglo[x+1]){
                if(!unaDiferente) {
                    unaDiferente = true;
                } else {
                    return false;
                }
            } else {
                x++;
            }
        }
    } else {
        for (int x = 0; x < arreglo.length; x++) {
            if (arreglo[x] != arreglo[x + 1]) {
                return false;
            } else {
                x++;
            }
        }
    }
    return true;
}
