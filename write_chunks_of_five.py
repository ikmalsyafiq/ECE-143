def write_chunks_of_five(words,fname):
    """write a chunk of five words per line into a file

    Args:
        words (list): list of words
        fname (str): string of name of the file
    """    
    assert isinstance(fname,str)
    assert isinstance(words,list)
    def divide_chunks(l, n): 
        """divide the words list into chunk of 5

        Args:
            l (list): [the list of words
            n (int): number of words per line

        Yields:
            list: list of words in multiple of 5
        """        
        # looping till length l
        for i in range(0, len(l), n): 
            yield l[i:i + n]
  
    x = list(divide_chunks(words, 5))
  
    outF = open(fname, "w")
    for i in x:
        line_of_5 =  ' '.join(i)
        print(line_of_5)
        outF.write(line_of_5)
        outF.write("\n")
    outF.close()   


  
