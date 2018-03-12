def isCaseInsensitivePalindrome(inputString):
    ns = inputString.lower()
    return ns[:]==ns[::-1]