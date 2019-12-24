def capitalizeVowelsRegExp(input):
    def vowel(m):
        v=m.group()
        return v.upper()
    p=re.compile('a|e|i|o|u|y')
    return p.sub(vowel, input)

def capitalizeVowels(input):
    vovel_list = ['a', 'e', 'i', 'o', 'u', 'y']
    return "".join([char.upper() if char in vovel_list else char for char in input])