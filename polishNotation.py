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
            stack = stack[:-3]
            stack.append(str(result))
            print(stack)
            
            

    return int(stack[0])

#tokens = ["+", "3", "7"] #10
#tokens = ["*", "-", "5", "6", "7"]  #-7
tokens = ["-", "5", "*", "6", "7"]  #37

print(polishNotation(tokens))




function polishNotation(tokens) {
  var isNumber = function(stringRepresentation) {
    return stringRepresentation.length > 1 ||
           '0' <= stringRepresentation[0] &&
           stringRepresentation[0] <= '9';
  };

  var stack = [];

  for (var i = 0; i < tokens.length; i++) {
    stack.push(tokens[i]);
    while (isNumber(stack[stack.length - 1])
     && isNumber(stack[stack.length - 2])) {
      var leftOperand = parseInt(stack[stack.length - 2]);
      var rightOperand = parseInt(stack[stack.length - 1]);
      var result = 0;
      if (stack[stack.length - 3] === '-') {
        result = leftOperand - rightOperand;
      }
      if (stack[stack.length - 3] === '+') {
        result = leftOperand + rightOperand;
      }
      if (stack[stack.length - 3] === '*') {
        result = leftOperand * rightOperand;
      }
      stack.splice(-3);
      stack.push(result.toString());
    }
  }

  return parseInt(stack[0]);
}
