def is_string_integer(str):
    """check if the string is an integer

    Args:
        str (string): a string 
    """    
    return str.isdecimal()

print(is_string_integer(' 123'))
