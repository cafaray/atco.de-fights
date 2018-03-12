def tennisSet(score1, score2):
    if (score1+score2)>=10 and min([score1, score2])>=5: 
        return True if score1 + score2 <= 13 and max([score1, score2])==7 and min([score1, score2])>=5 else 1 == 0
    return True if max([score1, score2]) == 6 and min([score1, score2]) < 5 else 1 == 0