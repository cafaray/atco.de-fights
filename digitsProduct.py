def digitsProduct(product):
    if product == 0: return 10
    if product < 10: return product
    number = list()
    while product > 1:
        
        for divisor in range(9, 1, -1):
            print('evaluating:',product, divisor)
            if product % divisor == 0:
                number.append(divisor)
                product /= divisor          
                if product < 10 and product > 1: 
                    number.append(int(product))
                    product = 1
                    #print(product)
                break
            else:
                if divisor == 2: 
                    return -1  # encontro un primo
                else:
                    continue
        if len(number) == 0: return -1
    res = ''
    for i in number: res = str(i) + res 
    return int(res)