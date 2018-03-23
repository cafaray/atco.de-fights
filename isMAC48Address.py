import re
def isMAC48Address(inputString):
    m = re.search('([0-9a-fA-F]{2}[\-]){5}([0-9a-fA-F]{2})$', inputString)
    
    if m is None:
        print(inputString, False)
        return False
    else:
        print(m.groups(0))
        print(m.groups(1))
        print(inputString, True)
        return True