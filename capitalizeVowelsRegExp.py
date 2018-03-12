def capitalizeVowelsRegExp(input):
    vovel_list = ['a', 'e', 'i', 'o', 'u', 'y']
    return "".join([char.upper() if char in vovel_list else char for char in input])