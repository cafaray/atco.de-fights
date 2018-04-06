def polishNotation(tokens):
    def isNumber(stringRepresentation):
        return (len(stringRepresentation) > 1 or
              '0' <= stringRepresentation[0] and
              stringRepresentation[0] <= '9')

    stack = []

    for i in range(len(tokens)):
        stack.append(tokens[i])        
        if (len(stack) > 2 and isNumber(stack[-1])
          and isNumber(stack[-2])):
            leftOperand = int(stack[-2])
            rightOperand = int(stack[-1])
            result = 0
            if stack[-3] == '-':
                result = leftOperand - rightOperand
            if stack[-3] == '+':
                result = leftOperand + rightOperand
            if stack[-3] == '*':
                result = leftOperand * rightOperand            
            tokens = stack[:-3]
            stack.append(str(result))
            print(stack)
            
            

    return int(stack[0])

#tokens = ["+", "3", "7"] #10
#tokens = ["*", "-", "5", "6", "7"]  #-7
tokens = ["-", "5", "*", "6", "7"]  #37

print(polishNotation(tokens))
