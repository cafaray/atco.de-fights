
bool primo(int x){
    if (x==1) return false;
    if (x==2) return true;
    if (x%2==0) return false;
    if (x==3) return true;
    for (int i=3; i*i<=x; i+=2)
        if (x%i==0) return false;
    return true;
}

int leastCommonPrimeDivisor(int a, int b) {
    int aux=-1;
    for(int i=2;i<=min(a,b);i++){
        if(primo(i) && a%i==0 && b%i==0){
            aux=i;
            break;
        }
    }
    return aux;
}