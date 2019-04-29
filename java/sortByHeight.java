int[] sortByHeight(int[] a) {
    int[] personas = new int[a.length];
    int x = 0;
    for(int e:a){
        if(e>-1){
            personas[x++] = e;
        }
    }
    x = personas.length - 1;
    Arrays.sort(personas);
    for(int i=a.length;i>0;i--){
        if(a[i-1]<0){
            //es un arbol
        } else {
            a[i-1] = personas[x--];				
        }
    }
    
    return a;
}