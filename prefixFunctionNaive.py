def prefixFunctionNaive(s):
    n = len(s)
    pi=[0]
    for i in range(1,n):
        l=0
        for k in range(i,i+1):
            sp=s[:k]
            ss=s[i-k+1:k]
            if sp==ss:
                l+=1
        pi+=[l]
    return pi


#        j = pi[i-1]
#        while (j > 0 && s[i] != s[j])
#            j = pi[j-1];
#        if (s[i] == s[j])
#            j++;
#        pi[i] = j;
#    }
#    return pi;


s= "acacbab"
response = [0, 0, 1, 2, 0, 1, 0]
print("Assertion is: ", prefixFunctionNaive(s)==response)