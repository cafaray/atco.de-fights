def findEmailDomain(address):
    dominio = ""
    print(len(address))
    for elemento in range(1, len(address)+1):
        posicion = len(address)-elemento
        if address[posicion] == '@': break
        dominio = address[posicion] + dominio
        print('dominio', dominio)
    return dominio