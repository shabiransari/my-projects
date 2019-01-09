import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np 
df_swing=pd.read_csv('E:\csvdhf5xlsxurlallfiles/2008_swing_states.csv')
print(df_swing.columns)
def ecdf(data):
	""" compute ecdf fo a one dimensional array of measurments"""
	n = len(data)
	x=np.sort(data)
	y=np.arange(1, n+1)/n 
	return x,y
x_dem_share, y_ecdf =ecdf(df_swing['dem_share'])
plt.plot(x_dem_share, y_ecdf, marker='.', color='red', linestyle='none')
plt.xlabel('percent vote for obama')
plt.ylabel('ECDF')
plt.show()
x_total_votes, y_ecdf=ecdf(df_swing['total_votes'])
plt.plot(x_total_votes, y_ecdf)
plt.xlabel('total_votes')
plt.ylabel('ECDF')
plt.show()
print(np.mean(df_swing['dem_share']))
#percentile computing
print(np.percentile(df_swing['dem_share'], [25, 50, 75, 100]))