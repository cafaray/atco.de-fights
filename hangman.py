S = set

hangman = lambda w,l:S(w)<=S(l[:len(S(w))+5])