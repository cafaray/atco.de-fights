int adjacentElementsProduct(int[] inputArray) {
    int max=Integer.MIN_VALUE, product=Integer.MIN_VALUE;
    for(int x=0;x<inputArray.length-1;x++){
        product = inputArray[x]*inputArray[x+1];
        if (product>max){
            max = product;
        }
    }
    return max;
}
