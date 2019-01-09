#introduction to flat files
#reading a txt file
#filename = 'HuckFinn.txt'with open(filename, 'r') as file:t = file.read()file.close()print(t)
#importing flat files using pandas
import pandas as pd 
data = pd.read_csv('E:\csvdhf5xlsxurlallfiles/winequality-red.csv', index_col=0)
print(data)
print(data.head())
df = pd.read_csv('E:\csvdhf5xlsxurlallfiles/titanic.csv')
print(df)
print(df.columns)
print(df.info())
import matplotlib.pyplot as plt 
ds=pd.read_csv('E:\csvdhf5xlsxurlallfiles/titanic_sub.csv')
print(ds)
print(ds.columns)
print(ds.head())
plt.hist(ds['Age'])
plt.show()
pd.DataFrame.hist(ds[['Age']])
plt.xlabel('Age')
plt.ylabel('count')
plt.show()
