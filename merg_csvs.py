import pandas as pd 
import glob

files = glob.glob('./Dataset/*.csv')

merged_data = pd.DataFrame()

for file in files:
    df = pd.read_csv(file)
    merged_data = pd.concat([merged_data, df])

merged_data.to_csv('merged_airline_delay_data.csv', index=False)