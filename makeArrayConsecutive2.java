int makeArrayConsecutive2(int[] statues) {
    Arrays.sort(statues);
    int missing = 0; 
    int min = statues[0], max = statues[statues.length -1];
    for (int x = 0;x<statues.length-1;x++){
        if(statues[x+1]!=(statues[x]+1)){
            missing+=(statues[x+1]-statues[x]-1);
        }
    }
    return missing;
}