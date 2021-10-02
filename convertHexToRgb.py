def convert_hex_to_RGB(list):
    """convert hex to rgb

    Args:
        list (list): a list of hex

    Returns:
        list : a list of rgb tuples
    """    
    rgb = []
    for i in list:
        h = i.lstrip('#')
        rgb.append(tuple(int(h[j:j+2], 16) for j in (0, 2, 4)))
    
    return rgb

