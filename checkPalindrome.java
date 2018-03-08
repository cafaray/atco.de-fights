boolean checkPalindrome(String inputString) {
    
    if (inputString.length()>1) {
    
        char[] word = inputString.toCharArray();
        int longitud = word.length/2;
        for(int x=0;x<longitud;x++){
            if(word[x]!=word[word.length-(x+1)]){
                return false;
            }
        }
    }
    return true;
        
    
}