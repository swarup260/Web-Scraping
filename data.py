import pandas as pd

df_json_raw = pd.read_json('anime_data.json')
df_json_raw.to_csv('data1.csv')
