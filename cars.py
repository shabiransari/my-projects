import pandas as pd 
cars = pd.read_csv('E:\csvdhf5xlsxurlallfiles/cars.csv', index_col=0)
print(cars)
print(cars.loc['US':'MOR'])
for lab, row in cars.iterrows():
	print(lab)
	print(row)
# filterring pandas dataframe
brics = pd.read_csv('E:\csvdhf5xlsxurlallfiles/brics.csv', index_col=0)
print(brics)
print(brics['area'])
print(brics['area']>8)
is_huge = brics['area']>8
print(brics[brics['area']>8])
print(brics[is_huge])
#area should be in b/w 8 and 10
import numpy as np 
And_m = brics[np.logical_and(brics['area']>8, brics['area']<10)]
print(And_m)
print(brics)
brics.loc[lab, 'name_length'] = len([["country"]])
print(brics)
#using pandas read_csv iterator for streaming data
df_reader = pd.read_csv('E:\csvdhf5xlsxurlallfiles\world_ind_pop_data.csv', index_col=0, chunksize=100)
print(next(df_reader))
print(next(df_reader).info())
print(next(df_reader).head(3))
print(next(df_reader).tail(2))
print(brics)
brics.loc[lab, 'name_length'] = len("country")
print(brics)  
