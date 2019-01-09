import pandas as pd 
import matplotlib.pyplot as plt 
stocks = pd.read_csv('E:\csvdhf5xlsxurlallfiles/stocks.csv', index_col=0)
print(stocks.head())
print(stocks.columns)
aapl= stocks['AAPL']
view=aapl['2007-11':'2008-4']
plt.plot(view, color='red')
plt.title('AAPL:Nov.2007 to Apr. 2008')
plt.show()
plt.plot(aapl)
plt.show()