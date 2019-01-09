import pandas as pd 
import matplotlib.pyplot as plt 
stocks = pd.read_csv('E:\csvdhf5xlsxurlallfiles/stocks.csv', index_col=0)
print(stocks.head())
print(stocks.columns)
aapl= stocks['AAPL']
plt.plot(aapl, color='blue', label='AAPL')
plt.plot(stocks['IBM'], color='green', label='IBM')
plt.plot(stocks['CSCO'], color='k', label='CSCO')
plt.plot(stocks['MSFT'], color='red', label='MSFT')
plt.legend(loc='upper left')
plt.xticks(rotation=60)
plt.show()