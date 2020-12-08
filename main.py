import pandas as pd 
import os
import get_metrics

#Config Variables:
relative_data_path = 'data.csv'

#Other Variables:
file_path = os.path.abspath(os.path.dirname(__file__))
data_loc = os.path.join(file_path, relative_data_path)

data_df = get_metrics.get_csv_data(data_loc)

print(data_df.head())