int arrayChange(int[] inputArray) {
    //Arrays.sort(inputArray);
    int iteraciones = 0;
    for(int x = 0; x<inputArray.length-1;x++){
        if(inputArray[x]<inputArray[x+1]){
            iteraciones+=0;
        } else{
            while(inputArray[x+1]<=inputArray[x]) {
                inputArray[x + 1]++;
                iteraciones++;
            }
        }
    }
    return iteraciones;
}