def validaPalindromo(inputString):
    return inputString == inputString[::-1]

def buildPalindrome(st):
    newString = ''
    initialLen = len(st)
    palindrome = st
    while validaPalindromo(palindrome) is False:
        newString = ''
        for i in range(0, len(st)+1):
            j = len(palindrome)-1-i
            if i > j: break
            if st[i] == st[j]:
                continue
            else:
                if j >= (initialLen - 1):
                    st = palindrome[:initialLen]
                    newString = palindrome[initialLen:]
                    #print('<<<< RETOMA VALORES[',j-initialLen + 1,']: \n\tst =', st,'\n\tnewString =', newString)
                    newString = newString[:j - initialLen+1] + palindrome[i] + newString[j-initialLen+1:]
                    #print('newString:', newString)
                    palindrome = st+newString
                    print('possible palindrome:', palindrome)
                    if validaPalindromo(palindrome) is True: 
                        return palindrome        
                    break
                else:
                    newString = st[i] + newString
                #print('newString:', newString)
            palindrome = st+newString
            print('possible palindrome:', palindrome)
            if validaPalindromo(palindrome) is True: 
                return palindrome        
        st = palindrome        
    return palindrome