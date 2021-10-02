def is_string_integer(str):
    """check if the string is an integer

    Args:
        str (string): a string 
    """    
    str = str.strip()
    return str.isdecimal()


