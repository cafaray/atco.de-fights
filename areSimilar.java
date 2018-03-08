boolean areSimilar(int[] a, int[] b) {
    boolean swap = false;
    for(int x = 0;x<a.length; x++){
        if(a[x]!=b[x]) {
            if (swap) return false;
            int swapItem = -1;
            for(int y=x;y<b.length;y++){
                if(b[y]==a[x] && b[y]!=a[y])swapItem = y;
            }
            //int posicion = contains(b, a[x]);
            //if(posicion>-1){
            if(swapItem>-1){
                int tmp = b[x];
                b[x] = a[x];
                b[swapItem] = tmp;
            } else {
                return false;
            }

            swap = true;
        }
    }
    return Arrays.equals(a,b);
}
