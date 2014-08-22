def char_conversion(arg):
    arg = arg.lower()
    if len(arg) > 1:
        arg = "z" #hardcoded to something that will cause an error
    arg = ord(arg) - 97
    return arg

def num_conversion(arg):
    arg = int(arg) - 1
    return arg