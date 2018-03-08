int commonCharacterCount(String s1, String s2) {

    char[] caracteres1 = s1.toCharArray();
    char[] caracteres2 = s2.toCharArray();
    Arrays.sort(caracteres1);
    Arrays.sort(caracteres2);
    int conteo = 0;
    int anterior = 0;
    for(char i: caracteres1){ 
        if(anterior>=caracteres2.length) return conteo;
        int howmany = howMany(i, caracteres2, anterior);
        anterior = (howmany<0?anterior:howmany+1);
        conteo += (howmany>=0?1:0);
    }
    return conteo;
}

int howMany(char i, char[] caracteres2, int start){
    
    for(int x = start;x<caracteres2.length;x++){
        if(i==caracteres2[x]){
            return x;
        }
    }
    return -1;
}