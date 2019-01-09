import pandas as pd 
import seaborn as sns 
import numpy as np 
import matplotlib.pyplot as plt 
df_all_states=pd.read_csv('E:\csvdhf5xlsxurlallfiles/2008_all_states.csv')
print(df_all_states.columns)
_=sns.boxplot(x='east_west', y='dem_share', data=df_all_states)
_=plt.xlabel('region')
_=plt.ylabel('percent vote for obama')
plt.show()
print(np.mean(df_all_states['dem_share']))
#variance and standard deviation
#. The mean squared distance of the data from their mean
# Informally, a measure of the spread of data
var_df_all_state= np.var(df_all_states['dem_share'])
print(var_df_all_state)
print(np.std(df_all_states['dem_share']))
print(np.sqrt(var_df_all_state))

