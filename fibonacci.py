def fibonacci(n):
    """the generator for fibonacci number

    Args:
        n (int): number of fibonacci number generated

    Yields:
        int: the fibonacci number
    """    
    assert isinstance(n,int)
    assert n>=0
    a, b = 0, 1
    for _ in range(n):
        
        a, b = b, a + b
        yield a

