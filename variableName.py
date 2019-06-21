def variableName(name):
    if '0' <= name[0] <= '9': return False
    for n in name:        
        if ('a' <= n <= 'z' or 'A' <=n <='Z' or '0' <= n <= '9') or n == '_':
            continue
        else:
            print(n)
            return False
    return True