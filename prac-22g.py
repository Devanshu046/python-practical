import pandas as pd
df=pd.read_csv('data.csv')
print(df.groupby('2010').mean().head())