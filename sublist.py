def all_sublists(s):
    """create a sublist of a list

    Args:
        s (list): list of things to be subset

    Returns:
        list: list of subsets

    """    
    assert isinstance(s,list)
    assert len(s)!=0
    assert len(s) == len(set(s))
    
    def powerset(s):
        """create a sublist of a list

        Args:
            s (list): list of things to be subset

        Yields:
            list: list of subsets
        """        
        x = len(s)
        masks = [1 << i for i in range(x)]
        for i in range(1,1 << x):
            yield [ss for mask, ss in zip(masks, s) if i & mask]
    return list(powerset(s))




 

