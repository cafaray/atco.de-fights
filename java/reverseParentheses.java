String reverseParentheses(String cadena){
    char[] caracteres = cadena.toCharArray();
    String nueva = "";
    for(int x = 0; x < cadena.length(); x++){
        char c = caracteres[x];
        if(c=='(') {
            String reves = reverseParentheses(cadena.substring(x+1));
            nueva += new StringBuilder("(".concat(reves)).toString();
            x += reves.length();
        } else if(c==')'){
            return new StringBuilder(nueva).reverse().toString().concat(")");
        } else {
            nueva += String.valueOf(c);
        }
    }
    return nueva.replaceAll("\\)*","").replaceAll("\\(*","");
}