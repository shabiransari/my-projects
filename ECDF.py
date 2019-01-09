import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np 
df_swing=pd.read_csv('E:\csvdhf5xlsxurlallfiles/2008_swing_states.csv')
print(df_swing.columns) 
x= np.sort(df_swing['dem_share'])
y=np.arange(1, len(x)+1)/len(x)
print(x)
print(y)
_=plt.plot(x, y, marker='.', linestyle='none')
_=plt.xlabel('percent of vote for obama')
_=plt.ylabel('ECDF')
plt.margins(0.02)
plt.show()