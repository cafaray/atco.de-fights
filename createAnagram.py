def createAnagram(s, t):
    count1 = [0]*26
    count2 = [0]*26
    
    for i in range(len(s)):
        count1[ord(s[i]) - ord('A')] += 1
        count2[ord(t[i]) - ord('A')] += 1
        
    ans = 0
    for i in range(26):
        ans += abs(count1[i] - count2[i])
        
    return ans//2