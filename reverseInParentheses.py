import re
# does not work
def reverseInParentheses(inputString):
    s=''
    for x in range(len(inputString)):
        if inputString[x]=='(':
            reverse = reverseInParentheses(inputString[x+1:])
            s+='('+reverse
            x+=len(reverse)
        elif inputString[x]==')':
            print('first:', s)
            s = re.sub(r"\).+", "", s)
            print('second', s)
            s = re.sub(r"\(.+", "", s)
            print('third', s)
            return s[::-1]+')'
        else:
            s += inputString[x]
            


print(reverseInParentheses('(bar)'))