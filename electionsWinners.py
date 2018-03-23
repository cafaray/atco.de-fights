def electionsWinners(votes, k):
    mini = min(votes)
    maxi = max(votes)
    if k == 0:     
        if mini==maxi:
            res = []
        else:
            res = [e for e in votes if e == maxi]       
            if len(res) > 1:
                res = []     
    else:
        maxi = maxi
        res = [e for e in votes if e + k > maxi]
    print(res)
    return(len(res))