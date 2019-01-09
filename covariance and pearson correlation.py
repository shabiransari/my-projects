import pandas as pd 
import seaborn as sns 
import numpy as np 
import matplotlib.pyplot as plt 
df_all_states=pd.read_csv('E:\csvdhf5xlsxurlallfiles/2008_all_states.csv')
print(df_all_states.columns)
_=plt.plot(df_all_states['total_votes']/1000, df_all_states['dem_share'], marker='.', linestyle='none')
_=plt.xlabel('total votes(thousands)')
_=plt.ylabel('present of vote for obama')
plt.show()
#covariance - a measure of how quantities vary together. covarience=1/n(sum(Xi-Xmean).(Yi-Ymean))
#r= correlation = covarience/(std of x)(std of y)
covarience_matrix=np.cov(df_all_states['total_votes'], df_all_states['dem_share'])
print(covarience_matrix)
cov = covarience_matrix[0,1]
print(cov)
def pearson_r(x,y):
	corr_mat=np.corroeff(x,y)
	return corr_mat[0,1]
r=pearson_r(df_all_states['total_votes'], df_all_states['dem_share'])
print(r)
