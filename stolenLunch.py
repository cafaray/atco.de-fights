def stolenLunch(note):
    note = note.lower()
    s=''
    for c in note:
        if 48<=ord(c)<=57:
            s+=chr(ord(c)+49)               
        else:
            if 97<=ord(c)<=106:
                s+=chr(ord(c)-49)
            else:
                s+=c
    return s