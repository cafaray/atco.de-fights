def unusualLexOrder(words):
    return [i[::-1] for i in sorted([j[::-1] for j in words])]