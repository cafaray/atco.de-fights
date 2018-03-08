def areSimilarNumbers(a, b, divisor):
    return (a%divisor == 0 and b%divisor== 0) or (a%divisor != 0 and b%divisor!= 0)