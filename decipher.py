def decipher(cipher):

    result = ''
    i = 0
    while i < len(cipher):
        if cipher[i] == '1':
            length = 3
        else:
            length = 2
        code = int(cipher[i : i + length])
        result += chr(code)
        i += length
    return result