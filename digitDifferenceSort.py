def digitDifferenceSort(a):
    difs = []
    res = []
    for x in range(len(a)):
        n = str(a[x])
        mx = max(list(n))
        mn = min(list(n))
        dif = int(mx) - int(mn)
        difs += [[dif, x]]
    difs = sorted(difs)
    for x in range(len(difs)-1):
        if a[difs[x][1]] == a[difs[x+1][1]]:
            print(a[difs[x][0]], a[difs[x+1][0]])
            rev = []
            tmp = x
            while a[difs[x][1]] == a[difs[x+1][1]]:
                rev += [a[difs[x][1]]]
                x+=1
            #res += rev.reverse() + [a[difs[tmp][1]]]
            continue
        res += [a[difs[x][1]]]
    print(res)