import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv')
print("First 5 rows: ",df.head())
print("First 10 rows: ",df.head(10))
print("Basic statistics: ",df.describe())
print("Last 5 rows: ",df.tail())
a=df.columns[2]
z=df[a]
print("Basic statistics: ",z.describe())