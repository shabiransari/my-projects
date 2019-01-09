import pandas as pdb
import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset('tips')
plt.subplot(1,2,1)
sns.boxplot(x='day', y='tip', data=tips)
plt.ylabel('tips($)')
plt.xlabel('Day')
plt.show()
plt.subplot(1,2,2)
sns.violinplot(x='day', y='tip', data=tips)
plt.ylabel('tips($)')
plt.xlabel('Day')
plt.tight_layout()
plt.show()
sns.violinplot(x='day', y='tip', data=tips,  inner=None, color='lightgray')
sns.stripplot(x='day', y='tip', data=tips, size=4, jitter=True)
sns.swarmplot(x='day', y='tip', data=tips, size=4, hue='sex', orient='v')#orient='h' for horizontal
plt.ylabel('tips($)')
plt.xlabel('Day')
plt.show()