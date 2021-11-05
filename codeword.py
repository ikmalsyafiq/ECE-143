
import numpy as np
import string
from string import punctuation
import random

def encrypt_message(message,fname):
    '''
  Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
  name of a text file source for the codebook, generate a sequence of 2-tuples that
  represents the `(line number, word number)` of each word in the message. The output is a list
  of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 
  7     
  :param message: message to encrypt
  :type message: str
 :param fname: filename for source text
 :type fname: str
 :returns: list of 2-tuples
   '''
    assert isinstance(fname,str)
    assert isinstance(message,str)
    
    def file_read(fname):
        content_array = []
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                
                        line_here = (line.lower().strip(punctuation).strip().split(" "))
                        line_here = [''.join(c for c in s if c not in string.punctuation) for s in line_here]
                        line_here = np.array(line_here)
                        
                        content_array.append(line_here)
                
                array = np.array(content_array)
                return array
    
    a = file_read(fname)
    words = message
    words_array = np.array(words.strip(punctuation).split(" "))

    tuple_code = []
    #print(a[0,0])
    for li in words_array:
        list_of_words = []
        for index, x in np.ndenumerate(a):
            if li in x:
                mnm = np.where(x==li)
                list_of_words.append((index[0]+1,mnm[0][0]+1))
        tuple_code.append(list_of_words)
    
    coded_messages = []
    for i in tuple_code:
        is_true = True
        while (is_true):
            assert len(i) != 0
            x_rand = i.pop()
            if x_rand not in coded_messages :
                coded_messages.append(x_rand)
                is_true = False
            
    return coded_messages


def decrypt_message(inlist,fname):
    '''
     Given `inlist`, which is a list of 2-tuples`fname` which is the
     name of a text file source for the codebook, return the encrypted message. 
     
     :param message: inlist to decrypt
     :type message: list
     :param fname: filename for source text
     :type fname: str
     :returns: string decrypted message
    '''
    assert isinstance(inlist,list)
    
    assert len(inlist) == len(set(inlist))
    
    assert isinstance(fname,str)
    
    def file_read(fname):
        content_array = []
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                
                        line_here = (line.lower().strip(punctuation).strip().split(" "))
                        line_here = [''.join(c for c in s if c not in string.punctuation) for s in line_here]
                        line_here = np.array(line_here)
                        
                        content_array.append(line_here)
                
                array = np.array(content_array)
                return array
    
    a = file_read(fname)
    
    decrypted_messages = []
    for ic in inlist:
        decrypted_messages.append(a[ic[0]-1][ic[1]-1])

    decrypted_string = ' '.join(decrypted_messages)
    return decrypted_string


