import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset('tips')#don't requred path
#visualization of univariate
#strip plot used for univatiet
sns.stripplot(y='tip',data=tips)
plt.ylabel('tip($)')
plt.show()
#grouping with striplpot
sns.stripplot(x='day', y='tip', data=tips)
plt.xlabel('Day')
plt.ylabel('tip($)')
plt.show()
sns.stripplot(x='day', y='tip', data=tips, size=10)
plt.xlabel('Day')
plt.ylabel('tip($)')
plt.show()


