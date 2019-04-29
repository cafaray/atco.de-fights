int[] alternatingSums(int[] a) {
    int[] output = new int[2];
    output[0] = 0;
    output[1] = 0;
    for(int x=0;x<a.length;x++){        
        if(x%2==0){
            output[0] += a[x];   
        } else {
            output[1] += a[x];
        }
    }
    return output;
}