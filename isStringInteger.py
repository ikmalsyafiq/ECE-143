def is_string_integer(string):
    """check if the string is an integer

    Args:
        string (string): a string 
    """    
    assert isinstance(string,str)
    string = string.strip()
    return string.isdecimal()




