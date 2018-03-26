def integerToStringOfFixedWidth(number, width):
    s = str(number)
    if width == len(s): return s
    if width < len(s): return s[width:]
    ceros = "0" * (width - len(s))
    return ceros + s