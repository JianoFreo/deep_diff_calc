

import pandas as pd


df = pd.read_csv('data cleaning/data/pokemon_data.csv')
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'

df.to_html('data cleaning/pandas/cleaned/test.html')
