import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
df_swing=pd.read_csv('E:\csvdhf5xlsxurlallfiles/2008_swing_states.csv')
print(df_swing.columns)
_=sns.swarmplot(x='state', y='dem_share', data=df_swing)
_=plt.xlabel('state')
_=plt.ylabel('percen of vote for obama')
plt.show()