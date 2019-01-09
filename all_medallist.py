import pandas as pd 
df = pd.read_csv('E:\csvdhf5xlsxurlallfiles/all_medalists.csv', index_col=0)
print(df.head)
print(df.head())
print(df.tail)
print(df.tail())
edition_col = df[['Edition']]
print(edition_co
