int shapeArea(int n) {
    if (n==1) return 1;
    int bloque = 0;
    int area = 0;
    for(int x=1;x<=n;x++){
        bloque = x + suma(x);
        area += bloque*2;
    }
    area -= bloque;
    return area;
}

int suma(int x){
    return x - 1;
}