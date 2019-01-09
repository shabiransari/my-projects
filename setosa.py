import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('E:\csvdhf5xlsxurlallfiles\stocks.csv')
print(df.head())
print(df.columns)
aapl=df['AAPL']
ibm=df['IBM']
print(type(aapl))
print(type(ibm))
print(aapl.shape)
print(ibm.shape)
plt.scatter(aapl, ibm, marker='o', color='red', label='stock1')
plt.legend(loc='upper right')
plt.show()