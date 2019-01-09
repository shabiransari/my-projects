import glob
import pandas as pd 
csv_files = glob.glob('*.csv')
print(csv_files)
#concatenation(combining of data) of data using pd.concat(filename)
list_data = []
for filename in  csv_files:
	data = pd.read_csv(filename, 'sort=True')
	list_data.append(data)
pd.concat(list_data)
pattern = '*.csv'
csv_files = glob.glob(pattern)
print(csv_files)
csv2 = pd.read_csv(csv_files[1])
print(csv2.head())
print(csv2.info())
print(csv2.tail)
print(csv2.head)
print(data.shape)
print(csv2.shape)
#another way of combining of data called merging pd.merg(left=..., right=..., left_on=..., right_on=...) especilly used for table combininng
# to check data types
print(data.dtypes)
#converting data types csv2["sulphates"] = csv2["sulphates"].astype('category')
print(type(data))
print(data)
#cleaning bad data (if a string(as '-' etc) present in column of  numeric data types called bad data) solution df['column name']=pd.to_numetic(df['columnname'], errors = 'coerce')
print(csv2.dtypes)
print(data.dtypes)
print(csv2.info())
import re
pattern = re.compile('\$\d*\.\d{2}')
result = pattern.match('$12.66')
print(bool(result))
prog = re.compile('\d{3}-\d{3}-\d{4}')
result = prog.match('788-566-7867')
result2 = prog.match('7868-566-7867')
print(result)
print(bool(result))
print(bool(result2))
matches = re.findall('\d+',' the recipe calls for 10 strawberries anD 1 banana')
print(matches)
#Usind functins to clean data df.apply(np.mean, axis=0)










