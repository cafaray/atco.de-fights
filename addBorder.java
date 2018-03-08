String[] addBorder(String[] picture) {
    
    String[] nuevo = new String[picture.length+2];
    int longitud = picture[0].length()+2;
    int posicion = 1;
    for(String cadena:picture){
        nuevo[posicion++] = "*".concat(cadena).concat("*");
    }
    nuevo[0] = "";
    for(int x=0;x<longitud;x++){
        nuevo[0] += "*";
    }
    nuevo[nuevo.length-1] = nuevo[0];
    return nuevo;
}