def symbolsPermutation(word1, word2):
    w1,w2=list(word1),list(word2)
    return sorted(w1)==sorted(w2)