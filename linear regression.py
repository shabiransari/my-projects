import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset('tips')#don't requred path
sns.lmplot(x='total_bill', y='tip', data=tips)#don't requred data series
plt.show()
#Using hue
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex')
plt.show()
#Using residplot()
print(tips.columns)
sns.residplot(x='tip', y='size', data=tips, color='red')
plt.show()
sns.regplot(x='total_bill', y='tip', data=tips, scatter=None, color='blue', label='order 1')
sns.regplot(x='total_bill', y='tip', data=tips, scatter=None, color='blue', label='order 2', order=2)
plt.legend(loc='upper left ')
plt.show()
sns.lmplot(x='total_bill', y='tip', data=tips, row='sex')
plt.show()





