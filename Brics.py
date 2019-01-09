import pandas as pd 
brics = pd.read_csv('E:\csvdhf5xlsxurlallfiles/brics.csv')#wrong indexed
print(brics)
brics = pd.read_csv('E:\csvdhf5xlsxurlallfiles/brics.csv', index_col=0)#correctly indexed
print(brics)
cars = pd.read_csv('E:\csvdhf5xlsxurlallfiles/cars.csv', index_col=0)
print(cars)


#column access[]
print(brics['country'])
print(brics['population'])
print(type(brics['population']))
print(brics[['country']])
print(type(brics[['country']]))
print(brics[['country', 'population']])
#row access
print(brics[1:5])
#powerfull tools access pandas rows 1 .loc[](labeled based), 2 .iloc[](indexed based)
#Row Access loc
print(brics.loc['RU'])
print(type(brics.loc['RU']))
print(brics.loc[['RU']])
print(type(brics.loc[['RU']]))
print(brics.loc[['BR', 'CH','IN']])
print(brics.loc[:, ['country', 'capital']])
print(type(brics.loc[:, ['country', 'capital']]))
#Row Access iloc[]
print(brics.iloc[1])
print(brics.iloc[[1,2,3],[0,1]])
print(cars)
print(cars.loc['MOR', 'drives_right'])
#comparision operators
print('arl'<'chrish')
#Filtering Pandas DataFrame
print(brics)
print(brics['area'])
print(brics['area']>8)
is_huge = brics['area']>8
print(brics[is_huge])
print(brics[brics['area']>8])
import numpy as np 
print(np.logical_and(brics['area']>8, brics['area']<10))
print(np.logical_or(brics['area']>8, brics['area']<10))
areas=[11.98, 89.0, 56.78]
for index, value in enumerate(areas):# enumerate used to unpack the element
	print(index+1, value)
#looping data structure
for val in brics:
	print(val)
#iterrows() is a powerfull tool to iterate the rows of dataframe
for lab, row in brics.iterrows():
	print(lab)
	print(row)
for lab, row in brics.iterrows():
	print(lab+':'+row['capital'])
#add a column
brics.loc[lab, 'name_length']=len(row['country'])
print(brics)
brics['name_length']=brics['country'].apply(len)
brics['capital_length']=brics['capital'].apply(len)
print(brics)










