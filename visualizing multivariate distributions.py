#1.jointplot, 2.pairsplots, 3.heatmaps
#jointplot
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
tips = sns.load_dataset('tips')
sns.jointplot(x='total_bill', y='tip', data=tips)
plt.show()
sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
plt.show()
#pairplot
sns.pairplot(tips)
plt.show()
#using pairplot with hue='sex'
sns.pairplot(tips, hue='sex')
plt.show()
#heatmap
#sns.heatmap('total_bill', 'tip', 'size')
#plt.show()
covarience=tips
print(covarience)
import numpy as np 
data_covarience=np.random.rand(4,4)
sns.heatmap(data_covarience)
plt.title('covarience')
plt.show()