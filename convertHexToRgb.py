def convert_hex_to_RGB(list_of_hex):
    """convert hex to rgb

    Args:
        list_of_hex (list): a list of hex

    Returns:
        list : a list of rgb tuples
    """ 
    assert isinstance(list_of_hex,list)  
    rgb = []
    for i in list_of_hex:
        h = i.lstrip('#')
        rgb.append(tuple(int(h[j:j+2], 16) for j in (0, 2, 4)))
    
    return rgb

print(convert_hex_to_RGB(['##ffaBB','##ffaBB']))




