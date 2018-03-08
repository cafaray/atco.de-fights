String[] allLongestStrings(String[] inputArray) {

    int max = 1;
    List<String> maxLengthArray = new ArrayList<>();
    for(String element: inputArray){
        if(element.length()>max){
            max = element.length();
            maxLengthArray = new ArrayList<>();
        }
        if(max==element.length()){
            maxLengthArray.add(element);
        }
    }
    return maxLengthArray.toArray(new String[maxLengthArray.size()]);
}