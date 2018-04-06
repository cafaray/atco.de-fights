def splitAddress(address):
    protocol = address[:address.find("://")]
    address = address[address.find("://")+3:]    
    domain = address[:address.find('.')]
    address = address[address.find('.'):]    
    res = [protocol, domain]
    if "/" in address:
        context = address[address.find('/')+1:]
        res += [context]
    return res