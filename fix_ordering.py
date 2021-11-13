import calendar
import pandas as pd
import pandas as pd

def add_month_yr(x):
    """add month and year column

    Args:
        x (dataframe): dataframe

    Returns:
        dataframe: dataframe with month-yr column
    """    
    assert isinstance(x,pd.DataFrame)
    x['Timestamp_stamp'] =pd.to_datetime(x['Timestamp'], format='%m/%d/%Y %H:%M',dayfirst=True) 
    x['Month'] = x['Timestamp_stamp'].dt.month
    x['Month'] = x['Month'].apply(lambda x: calendar.month_abbr[x])
    x['Year'] = x['Timestamp_stamp'].dt.year
    x['month-yr'] =  x["Month"] +'-'+x["Year"].astype(str)
    x = x.drop(['Timestamp_stamp', 'Month', 'Year'], axis=1)
    return x


def fix_categorical(x):
    """fix the order of the month-yr

    Args:
        x (dataframe): dataframe with month-yr column

    Returns:
        dataframe: with month-yr ordered
    """    
    assert isinstance(x,pd.DataFrame)
    x['month-yr'] = pd.Categorical(x['month-yr'],categories= x['month-yr'].unique(),ordered=True)
    return x

