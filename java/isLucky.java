boolean isLucky(int n) {
    String numero = String.valueOf(n);	    
    char[] digitos = numero.toCharArray();
	int suma1 = 0, suma2 = 0;
	for(int x=0;x<digitos.length/2;x++){
	    suma1 += Integer.parseInt(String.valueOf(digitos[x]));
	    suma2 += Integer.parseInt(String.valueOf(digitos[digitos.length - (x+1)]));
	}
	return (suma1==suma2);
}