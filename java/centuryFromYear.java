int centuryFromYear(int year) {
    int century = year /100;
    century+=(year%100>0?1:0);
    return century;
}