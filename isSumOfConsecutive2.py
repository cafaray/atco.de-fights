def isSumOfConsecutive2(n):
    return len([n//(x+1) for x in range(0 ,n) if n%(x+1)==0 and n//(x+1)>1 and n//(x+1)%2!=0])