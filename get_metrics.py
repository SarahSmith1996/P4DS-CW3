import os
import pandas as pd




#Functions:

def get_csv_data(location):

    df = pd.read_csv(location)
    return df

