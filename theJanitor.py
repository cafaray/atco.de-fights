def theJanitor(word):

    left = [0] * 26
    right = [0] * 26
    was = [0] * 26
    for i in range(26):
        left.append(0)
        right.append(0)
        was.append(False)

    for i in range(len(word)):
        c = ord(word[i]) - ord('a')
        if not was[c]:
            left[c] = i
            was[c] = True
        right[c] = i

    ans = []
    for i in range(26):
        ans.append(right[i] - left[i] + 1 if was[i] else 0)
    return anss