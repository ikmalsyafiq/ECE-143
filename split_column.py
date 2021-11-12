import pandas as pd
from itertools import chain
import collections

def  split_count(x):
    """split out column entries

    Args:
        x (dataframe): dataframe

    Returns:
        dataframe: dataframe with count
    """    
    assert isinstance(x,pd.Series)
    splitted = []
    for i in x:
        splitted.append(i.split(','))
        y = list(chain.from_iterable(splitted))
    #print()
    counter=collections.Counter(y)
    counter
    data = pd.DataFrame(counter.items())
    data = data.rename(columns={0: '', 1: 'Count'})
    data = data.sort_values(by = ['Count'],ascending=True)
    data.reset_index(drop=True, inplace=True)
    return data






