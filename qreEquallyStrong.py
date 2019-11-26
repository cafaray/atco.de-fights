A=eval(dir()[0])
return (A[0]==A[2] or A[0]==A[3]) and (A[1]==A[3] or A[1]==A[2])

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return (yourLeft==friendsLeft or yourLeft==friendsRight) and (yourRight==friendsRight or yourRight==friendsLeft)