import pandas as pd 
import numpy as np 
baseball = pd.read_csv('E:\csvdhf5xlsxurlallfiles/baseball.csv', index_col=0)
print(baseball)
print(baseball.columns)
print(baseball.info())
ext_height=baseball['Height']
print(ext_height)
height_array = np.array(ext_height)
mult = height_array*5
print(mult)
for i in mult :
	if i>=360:
		print(i)
	else:
		print("they will not play")
ext_weight = baseball['Weight']
weight_array = np.array(ext_weight)
bmi=weight_array/height_array**2
print(bmi)
for j in bmi:
	if j>=0.03287071:
		print('selected')
	else:
		print('not selected')
print(baseball.head(10))
print(baseball.tail(10))
ext_PostCategory=baseball['PosCategory']
for k in ext_PostCategory:
	if k=='Infielder':
		print((k))
print(baseball.index)
print(baseball.head)
print(baseball.loc['Josh_Kinney'])
